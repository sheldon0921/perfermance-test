#!/usr/bin/env bash
set -euo pipefail
export LANG="${LANG:-en_US.UTF-8}"
export LC_ALL="${LC_ALL:-en_US.UTF-8}"

ALLURE_RESULTS_DIR="${ALLURE_RESULTS_DIR:-report/allure-results}"
NEWMAN_XML_DIR="${RESULT_DIR:-report/result}"
JMETER_JTL_FILE="${JTL_FILE:-report/jtlResult.jtl}"
JMETER_STATS_FILE="${REPORT_DIR:-report/report}/statistics.json"
TEST_TYPE="${TEST_TYPE:-unknown}"

if [ -z "$ALLURE_RESULTS_DIR" ] || [ "$ALLURE_RESULTS_DIR" = "/" ] || [ "$ALLURE_RESULTS_DIR" = "." ]; then
  echo "Refusing to use unsafe Allure results directory: $ALLURE_RESULTS_DIR"
  exit 1
fi

rm -rf "$ALLURE_RESULTS_DIR"
mkdir -p "$ALLURE_RESULTS_DIR"

ruby -Ku - "$ALLURE_RESULTS_DIR" "$NEWMAN_XML_DIR" "$JMETER_JTL_FILE" "$JMETER_STATS_FILE" "$TEST_TYPE" <<'RUBY'
# encoding: UTF-8
require 'csv'
require 'digest'
require 'json'
require 'rexml/document'
require 'securerandom'
require 'time'

allure_dir, newman_xml_dir, jmeter_jtl_file, jmeter_stats_file, test_type = ARGV

def now_ms
  (Time.now.to_f * 1000).to_i
end

def ms_from_time(value)
  (value.to_f * 1000).to_i
end

def uuid_for(*parts)
  Digest::MD5.hexdigest(parts.join('|'))
end

def write_result(dir, result)
  File.write(File.join(dir, "#{result[:uuid]}-result.json"), JSON.pretty_generate(result))
end

def status_from_failure(failure)
  failure ? 'failed' : 'passed'
end

if ['postman', 'unknown', 'local', ''].include?(test_type)
  Dir.glob(File.join(newman_xml_dir, '*.xml')).sort.each do |xml_path|
    doc = REXML::Document.new(File.read(xml_path))
    collection = doc.root.attributes['name'].to_s
    collection = File.basename(xml_path, '.xml') if collection.empty?

    REXML::XPath.match(doc, '//testcase').each do |testcase|
      suite = testcase.parent.attributes['name'].to_s
      assertion = testcase.attributes['name'].to_s
      classname = testcase.attributes['classname'].to_s
      failure = REXML::XPath.first(testcase, 'failure|error')
      started = begin
        timestamp = testcase.parent.attributes['timestamp'].to_s
        timestamp.empty? ? now_ms : (Time.parse(timestamp).to_f * 1000).to_i
      rescue
        now_ms
      end
      duration = ms_from_time(testcase.attributes['time'].to_s)
      name = "#{suite} - #{assertion}"

      result = {
        uuid: uuid_for('postman', collection, suite, assertion, classname),
        historyId: uuid_for('history', 'postman', collection, suite, assertion, classname),
        testCaseId: uuid_for('case', 'postman', collection, suite, assertion, classname),
        name: name,
        fullName: "#{collection}.#{suite}.#{assertion}",
        status: status_from_failure(failure),
        statusDetails: failure ? { message: failure.attributes['message'].to_s, trace: failure.text.to_s } : {},
        stage: 'finished',
        start: started,
        stop: started + duration,
        labels: [
          { name: 'framework', value: 'Newman' },
          { name: 'language', value: 'Postman' },
          { name: 'suite', value: collection },
          { name: 'parentSuite', value: 'Postman' },
          { name: 'subSuite', value: suite },
          { name: 'package', value: classname.empty? ? collection : classname }
        ],
        parameters: [
          { name: 'collection', value: collection },
          { name: 'request', value: suite }
        ]
      }
      write_result(allure_dir, result)
    end
  end
end

if ['jmeter', 'unknown', 'local', ''].include?(test_type) && File.exist?(jmeter_jtl_file)
  rows = CSV.read(jmeter_jtl_file, headers: true)
  rows.each_with_index do |row, index|
    label = row['label'].to_s.empty? ? "sample-#{index + 1}" : row['label'].to_s
    success = row['success'].to_s.downcase == 'true'
    started = row['timeStamp'].to_i
    elapsed = row['elapsed'].to_i
    response_code = row['responseCode'].to_s
    response_message = row['responseMessage'].to_s
    thread_name = row['threadName'].to_s

    result = {
      uuid: uuid_for('jmeter', index, label, started, elapsed),
      historyId: uuid_for('history', 'jmeter', label),
      testCaseId: uuid_for('case', 'jmeter', label),
      name: label,
      fullName: "JMeter.#{label}",
      status: success ? 'passed' : 'failed',
      statusDetails: success ? {} : { message: "#{response_code} #{response_message}".strip },
      stage: 'finished',
      start: started,
      stop: started + elapsed,
      labels: [
        { name: 'framework', value: 'JMeter' },
        { name: 'language', value: 'JMX' },
        { name: 'suite', value: 'JMeter' },
        { name: 'parentSuite', value: 'JMeter' },
        { name: 'subSuite', value: label }
      ],
      parameters: [
        { name: 'responseCode', value: response_code },
        { name: 'responseMessage', value: response_message },
        { name: 'threadName', value: thread_name },
        { name: 'elapsedMs', value: elapsed.to_s }
      ]
    }
    write_result(allure_dir, result)
  end
end

environment = {
  'TEST_TYPE' => test_type,
  'Generated At' => Time.now.strftime('%Y-%m-%d %H:%M:%S'),
  'Newman Results' => File.exist?(newman_xml_dir) ? newman_xml_dir : '',
  'JMeter JTL' => File.exist?(jmeter_jtl_file) ? jmeter_jtl_file : ''
}
File.write(File.join(allure_dir, 'environment.properties'), environment.map { |k, v| "#{k}=#{v}" }.join("\n"))

if File.exist?(jmeter_stats_file)
  stats = JSON.parse(File.read(jmeter_stats_file))
  total = stats['Total'] || stats.values.first
  if total
    summary = [
      "# JMeter Summary",
      "",
      "| Metric | Value |",
      "| --- | --- |",
      "| Samples | #{total['sampleCount']} |",
      "| Errors | #{total['errorCount']} |",
      "| Error Rate | #{total['errorPct']}% |",
      "| Avg Response | #{total['meanResTime']} ms |",
      "| P90 | #{total['pct1ResTime']} ms |",
      "| P95 | #{total['pct2ResTime']} ms |",
      "| P99 | #{total['pct3ResTime']} ms |",
      "| Throughput | #{total['throughput']}/s |"
    ].join("\n")
    File.write(File.join(allure_dir, 'jmeter-summary.md'), summary)
  end
end

puts "Allure results: #{allure_dir}"
RUBY
