#!/usr/bin/env bash
set -euo pipefail
export LANG="${LANG:-en_US.UTF-8}"
export LC_ALL="${LC_ALL:-en_US.UTF-8}"

REPORT_HOME="${REPORT_HOME:-report/jenkins}"
NEWMAN_XML_DIR="${RESULT_DIR:-report/result}"
NEWMAN_HTML_DIR="${HTML_DIR:-report/newman}"
JMETER_REPORT_DIR="${REPORT_DIR:-report/report}"
JMETER_JTL_FILE="${JTL_FILE:-report/jtlResult.jtl}"
ALLURE_REPORT_DIR="${ALLURE_REPORT_DIR:-report/allure-report}"
TEST_TYPE="${TEST_TYPE:-unknown}"
INDEX_FILE="$REPORT_HOME/index.html"

if [ -z "$REPORT_HOME" ] || [ "$REPORT_HOME" = "/" ] || [ "$REPORT_HOME" = "." ]; then
  echo "Refusing to use unsafe report home: $REPORT_HOME"
  exit 1
fi

if [ "$TEST_TYPE" = "postman" ] || [ "$TEST_TYPE" = "local" ] || [ "$TEST_TYPE" = "unknown" ] || [ -z "$TEST_TYPE" ]; then
  if [ -z "$NEWMAN_HTML_DIR" ] || [ "$NEWMAN_HTML_DIR" = "/" ] || [ "$NEWMAN_HTML_DIR" = "." ]; then
    echo "Refusing to use unsafe Newman HTML directory: $NEWMAN_HTML_DIR"
    exit 1
  fi
fi

rm -rf "$REPORT_HOME"
mkdir -p "$REPORT_HOME"

ruby -Ku - "$INDEX_FILE" "$NEWMAN_XML_DIR" "$NEWMAN_HTML_DIR" "$JMETER_REPORT_DIR" "$JMETER_JTL_FILE" "$ALLURE_REPORT_DIR" "$TEST_TYPE" "${BUILD_NUMBER:-local}" "${JOB_NAME:-local}" <<'RUBY'
# encoding: UTF-8
require 'cgi'
require 'fileutils'
require 'json'
require 'rexml/document'
require 'time'

index_file, newman_xml_dir, newman_html_dir, jmeter_report_dir, jmeter_jtl_file, allure_report_dir, test_type, build_number, job_name = ARGV

def h(value)
  CGI.escapeHTML(value.to_s)
end

def rel_from_index(path)
  Pathname.new(File.expand_path(path)).relative_path_from(Pathname.new(File.expand_path(File.dirname(ARGV[0])))).to_s
rescue
  path
end

def rel_between(from_dir, path)
  Pathname.new(File.expand_path(path)).relative_path_from(Pathname.new(File.expand_path(from_dir))).to_s
rescue
  path
end

def fmt_number(value, digits = 2)
  return '-' if value.nil?
  number = value.to_f
  rounded = number.round(digits)
  rounded == rounded.to_i ? rounded.to_i.to_s : rounded.to_s
end

require 'pathname'

show_newman = ['postman', 'unknown', 'local', ''].include?(test_type)
show_jmeter = ['jmeter', 'unknown', 'local', ''].include?(test_type)
generated_at = Time.now.strftime('%Y-%m-%d %H:%M:%S')
warnings = []

newman_css_file = File.join(newman_html_dir, 'newman.css')
newman_css = <<~CSS
:root {
  color-scheme: light;
  --bg: #f6f8fb;
  --panel: #ffffff;
  --ink: #172033;
  --muted: #657188;
  --line: #d9e0ea;
  --ok: #0f8f63;
  --bad: #c83b3b;
  --accent: #2368b2;
}
* { box-sizing: border-box; }
body {
  margin: 0;
  background: var(--bg);
  color: var(--ink);
  font: 14px/1.5 -apple-system, BlinkMacSystemFont, "Segoe UI", Arial, sans-serif;
}
main { max-width: 1120px; margin: 0 auto; padding: 28px 20px 40px; }
header { display: flex; justify-content: space-between; gap: 16px; align-items: flex-start; margin-bottom: 22px; }
h1 { margin: 0 0 6px; font-size: 26px; line-height: 1.2; letter-spacing: 0; }
h2 { margin: 0 0 12px; font-size: 17px; letter-spacing: 0; }
.subtle { color: var(--muted); }
.badge {
  display: inline-flex; align-items: center; min-height: 30px; padding: 0 12px;
  border-radius: 999px; font-weight: 700; background: #e8f5ef; color: var(--ok);
}
.badge.failed { background: #fdecec; color: var(--bad); }
.grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 12px; margin: 18px 0; }
.card, section { background: var(--panel); border: 1px solid var(--line); border-radius: 8px; }
.card { padding: 14px; }
.metric { color: var(--muted); font-size: 12px; text-transform: uppercase; }
.value { margin-top: 4px; font-size: 24px; font-weight: 750; }
section { padding: 18px; margin-top: 16px; }
table { width: 100%; border-collapse: collapse; }
th, td { padding: 10px 8px; border-bottom: 1px solid var(--line); text-align: left; vertical-align: top; }
th { color: var(--muted); font-size: 12px; text-transform: uppercase; }
tr:last-child td { border-bottom: 0; }
a { color: var(--accent); text-decoration: none; font-weight: 650; }
a:hover { text-decoration: underline; }
.passed { color: var(--ok); font-weight: 700; }
.failed { color: var(--bad); font-weight: 700; }
.back { display: inline-flex; margin-bottom: 14px; }
.failure { margin-top: 8px; padding: 10px; border-radius: 6px; background: #fdecec; white-space: pre-wrap; }
@media (max-width: 640px) {
  header { display: block; }
  .badge { margin-top: 12px; }
  th:nth-child(3), td:nth-child(3) { display: none; }
}
CSS
if show_newman
  FileUtils.mkdir_p(newman_html_dir)
  File.write(newman_css_file, newman_css)
end

newman_reports = show_newman ? Dir.glob(File.join(newman_xml_dir, '*.xml')).sort.map do |xml_path|
  doc = REXML::Document.new(File.read(xml_path))
  suites = REXML::XPath.match(doc, '//testsuite')
  tests = suites.sum { |suite| suite.attributes['tests'].to_i }
  failures = suites.sum { |suite| suite.attributes['failures'].to_i + suite.attributes['errors'].to_i }
  skipped = suites.sum { |suite| suite.attributes['skipped'].to_i }
  duration = suites.sum { |suite| suite.attributes['time'].to_f }
  name = File.basename(xml_path, '.xml')
  html_path = File.join(newman_html_dir, "#{name}.html")
  back_href = rel_between(File.dirname(html_path), index_file)
  cases = REXML::XPath.match(doc, '//testcase').map do |testcase|
    failure = REXML::XPath.first(testcase, 'failure|error')
    {
      suite: testcase.parent.attributes['name'].to_s,
      name: testcase.attributes['name'].to_s,
      classname: testcase.attributes['classname'].to_s,
      time: testcase.attributes['time'].to_f,
      status: failure ? 'Failed' : 'Passed',
      failure: failure&.text.to_s
    }
  end
  detail_cards = [
    ['Requests', suites.length],
    ['Assertions', tests],
    ['Failures', failures],
    ['Skipped', skipped],
    ['Duration', "#{fmt_number(duration, 3)} s"]
  ]
  detail_rows = cases.map do |testcase|
    status_class = testcase[:status] == 'Passed' ? 'passed' : 'failed'
    failure_block = testcase[:failure].empty? ? '' : %(<div class="failure">#{h(testcase[:failure])}</div>)
    %(<tr><td>#{h(testcase[:suite])}</td><td>#{h(testcase[:name])}#{failure_block}</td><td>#{h(testcase[:classname])}</td><td>#{h(fmt_number(testcase[:time], 3))} s</td><td class="#{status_class}">#{h(testcase[:status])}</td></tr>)
  end.join("\n")
  detail_html = <<~HTML
  <!doctype html>
  <html lang="zh-CN">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Newman Report - #{h(name)}</title>
    <link rel="stylesheet" href="newman.css">
  </head>
  <body>
    <main>
      <a class="back" href="#{h(back_href)}">Back to Test Report</a>
      <header>
        <div>
          <h1>#{h(name)}</h1>
          <div class="subtle">Collection: #{h(doc.root.attributes['name'])} · Generated: #{h(generated_at)}</div>
        </div>
        <div class="badge #{failures.zero? ? '' : 'failed'}">#{failures.zero? ? 'Passed' : 'Failed'}</div>
      </header>
      <div class="grid">
        #{detail_cards.map { |label, value| %(<div class="card"><div class="metric">#{h(label)}</div><div class="value">#{h(value)}</div></div>) }.join("\n        ")}
      </div>
      <section>
        <h2>Assertions</h2>
        <table>
          <thead><tr><th>Request</th><th>Assertion</th><th>Class</th><th>Duration</th><th>Status</th></tr></thead>
          <tbody>#{detail_rows}</tbody>
        </table>
      </section>
    </main>
  </body>
  </html>
  HTML
  File.write(html_path, detail_html)
  {
    name: name,
    tests: tests,
    failures: failures,
    skipped: skipped,
    duration: duration,
    html: File.exist?(html_path) ? rel_from_index(html_path) : nil
  }
rescue => e
  warnings << "Could not read Newman XML #{xml_path}: #{e.class}: #{e.message}"
  {
    name: File.basename(xml_path, '.xml'),
    tests: 0,
    failures: 1,
    skipped: 0,
    duration: 0,
    html: nil,
    error: e.message
  }
end : []

jmeter_stats_path = File.join(jmeter_report_dir, 'statistics.json')
jmeter_total = nil
if show_jmeter && File.exist?(jmeter_stats_path)
  begin
    stats = JSON.parse(File.read(jmeter_stats_path))
    jmeter_total = stats['Total'] || stats.values.first
  rescue => e
    warnings << "Could not read JMeter statistics: #{e.class}: #{e.message}"
  end
end

newman_total_tests = newman_reports.sum { |report| report[:tests] }
newman_total_failures = newman_reports.sum { |report| report[:failures] }
newman_total_skipped = newman_reports.sum { |report| report[:skipped] }
has_newman_report = newman_reports.any?
has_jmeter_report = !jmeter_total.nil?
has_any_report = has_newman_report || has_jmeter_report
has_failure = (has_newman_report && newman_total_failures.positive?) ||
              (has_jmeter_report && jmeter_total['errorCount'].to_i.positive?)
status_text = if has_failure
                'Failed'
              elsif has_any_report
                'Passed'
              else
                'No report'
              end

jmeter_dashboard = show_jmeter && File.exist?(File.join(jmeter_report_dir, 'index.html')) ? rel_from_index(File.join(jmeter_report_dir, 'index.html')) : nil
jtl_link = show_jmeter && File.exist?(jmeter_jtl_file) ? rel_from_index(jmeter_jtl_file) : nil
allure_report = File.exist?(File.join(allure_report_dir, 'index.html')) ? rel_from_index(File.join(allure_report_dir, 'index.html')) : nil

cards = []
if has_newman_report
  cards << ['Collections', newman_reports.length]
  cards << ['Assertions', newman_total_tests]
  cards << ['Failures', newman_total_failures]
  cards << ['Skipped', newman_total_skipped]
end
if has_jmeter_report
  cards << ['Samples', jmeter_total['sampleCount']]
  cards << ['Error Rate', "#{fmt_number(jmeter_total['errorPct'])}%"]
  cards << ['Avg Response', "#{fmt_number(jmeter_total['meanResTime'])} ms"]
  cards << ['Throughput', "#{fmt_number(jmeter_total['throughput'])}/s"]
end

css_file = File.join(File.dirname(index_file), 'style.css')
css = <<~CSS
:root {
  color-scheme: light;
  --bg: #f6f8fb;
  --panel: #ffffff;
  --ink: #172033;
  --muted: #657188;
  --line: #d9e0ea;
  --ok: #0f8f63;
  --bad: #c83b3b;
  --accent: #2368b2;
}
* { box-sizing: border-box; }
body {
  margin: 0;
  background: var(--bg);
  color: var(--ink);
  font: 14px/1.5 -apple-system, BlinkMacSystemFont, "Segoe UI", Arial, sans-serif;
}
main { max-width: 1120px; margin: 0 auto; padding: 28px 20px 40px; }
header { display: flex; justify-content: space-between; gap: 16px; align-items: flex-start; margin-bottom: 22px; }
h1 { margin: 0 0 6px; font-size: 26px; line-height: 1.2; letter-spacing: 0; }
h2 { margin: 0 0 12px; font-size: 17px; letter-spacing: 0; }
.subtle { color: var(--muted); }
.badge {
  display: inline-flex; align-items: center; min-height: 30px; padding: 0 12px;
  border-radius: 999px; font-weight: 700; background: #e8f5ef; color: var(--ok);
}
.badge.failed { background: #fdecec; color: var(--bad); }
.grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 12px; margin: 18px 0; }
.card, section { background: var(--panel); border: 1px solid var(--line); border-radius: 8px; }
.card { padding: 14px; }
.metric { color: var(--muted); font-size: 12px; text-transform: uppercase; }
.value { margin-top: 4px; font-size: 24px; font-weight: 750; }
section { padding: 18px; margin-top: 16px; }
table { width: 100%; border-collapse: collapse; }
th, td { padding: 10px 8px; border-bottom: 1px solid var(--line); text-align: left; }
th { color: var(--muted); font-size: 12px; text-transform: uppercase; }
tr:last-child td { border-bottom: 0; }
a { color: var(--accent); text-decoration: none; font-weight: 650; }
a:hover { text-decoration: underline; }
.actions { display: flex; flex-wrap: wrap; gap: 10px; }
.button {
  display: inline-flex; align-items: center; min-height: 34px; padding: 0 12px;
  border: 1px solid var(--line); border-radius: 6px; background: #fff;
}
.empty { color: var(--muted); padding: 10px 0; }
@media (max-width: 640px) {
  header { display: block; }
  .badge { margin-top: 12px; }
  th:nth-child(4), td:nth-child(4) { display: none; }
}
CSS

html = <<~HTML
<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Test Report - #{h(job_name)} ##{h(build_number)}</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <main>
    <header>
      <div>
        <h1>#{h(job_name)} ##{h(build_number)}</h1>
        <div class="subtle">Type: #{h(test_type)} · Generated: #{h(generated_at)}</div>
      </div>
      <div class="badge #{status_text == 'Failed' ? 'failed' : ''}">#{h(status_text)}</div>
    </header>

    <div class="grid">
      #{cards.map { |label, value| %(<div class="card"><div class="metric">#{h(label)}</div><div class="value">#{h(value)}</div></div>) }.join("\n      ")}
    </div>

    <section>
      <h2>Report Links</h2>
      <div class="actions">
        #{allure_report ? %(<a class="button" href="#{h(allure_report)}">Allure Report</a>) : ''}
        #{newman_reports.map { |report| report[:html] ? %(<a class="button" href="#{h(report[:html])}">#{h(report[:name])} HTML</a>) : nil }.compact.join("\n        ")}
        #{jmeter_dashboard ? %(<a class="button" href="#{h(jmeter_dashboard)}">JMeter Dashboard</a>) : ''}
        #{jtl_link ? %(<a class="button" href="#{h(jtl_link)}">JMeter JTL</a>) : ''}
      </div>
      #{warnings.any? ? %(<div class="empty">#{h(warnings.join(' | '))}</div>) : ''}
      #{!has_any_report && !jmeter_dashboard ? '<div class="empty">No detailed report files were generated for this build.</div>' : ''}
    </section>

    #{if show_newman
        body = if newman_reports.any?
                 rows = newman_reports.map do |report|
                   result = report[:failures].zero? ? 'Passed' : 'Failed'
                   link = report[:html] ? %(<a href="#{h(report[:html])}">Open</a>) : '-'
                   %(<tr><td>#{h(report[:name])}</td><td>#{h(report[:tests])}</td><td>#{h(report[:failures])}</td><td>#{h(fmt_number(report[:duration], 3))} s</td><td>#{h(result)}</td><td>#{link}</td></tr>)
                 end.join("\n")
                 %(<table><thead><tr><th>Collection</th><th>Tests</th><th>Failures</th><th>Duration</th><th>Result</th><th>HTML</th></tr></thead><tbody>#{rows}</tbody></table>)
               else
                 '<div class="empty">No Newman JUnit XML found.</div>'
               end
        %(<section><h2>Newman Summary</h2>#{body}</section>)
      end}

    #{if show_jmeter
        body = if jmeter_total
                 %(<table><tbody>
                   <tr><th>Samples</th><td>#{h(jmeter_total['sampleCount'])}</td><th>Errors</th><td>#{h(jmeter_total['errorCount'])}</td></tr>
                   <tr><th>Error Rate</th><td>#{h(fmt_number(jmeter_total['errorPct']))}%</td><th>Throughput</th><td>#{h(fmt_number(jmeter_total['throughput']))}/s</td></tr>
                   <tr><th>Avg Response</th><td>#{h(fmt_number(jmeter_total['meanResTime']))} ms</td><th>Median</th><td>#{h(fmt_number(jmeter_total['medianResTime']))} ms</td></tr>
                   <tr><th>P90</th><td>#{h(fmt_number(jmeter_total['pct1ResTime']))} ms</td><th>P95</th><td>#{h(fmt_number(jmeter_total['pct2ResTime']))} ms</td></tr>
                   <tr><th>P99</th><td>#{h(fmt_number(jmeter_total['pct3ResTime']))} ms</td><th>Max</th><td>#{h(fmt_number(jmeter_total['maxResTime']))} ms</td></tr>
                 </tbody></table>)
               else
                 '<div class="empty">No JMeter statistics.json found.</div>'
               end
        %(<section><h2>JMeter Summary</h2>#{body}</section>)
      end}
  </main>
</body>
</html>
HTML

File.write(css_file, css)
File.write(index_file, html)
puts "Report index: #{index_file}"
RUBY
