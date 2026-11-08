// Regenerates section 7 of CLAUDE.md (the roadmap reference) from the data inside index.html
// and the counts in flashcards.json and practice/tasks.json,
// so the handoff file always matches what the app shows. Sections 1-6 are kept as written.
// Run from the repo root:  node tools/update-claude-md.js
const fs = require("fs");
const path = require("path");

const root = path.resolve(__dirname, "..");
const htmlPath = path.join(root, "index.html");
const mdPath = path.join(root, "CLAUDE.md");
const MARKER = "## 7. Roadmap reference";

const html = fs.readFileSync(htmlPath, "utf8");
const start = html.indexOf("const SECTIONS");
const end = html.indexOf("const resources = RES.map");
if (start < 0 || end < 0) throw new Error("Could not find the data block in index.html");
const { SECTIONS, LEVELS, T, LANES, STAGES, KINDS, RES, LC } =
  new Function(html.slice(start, end) + "\nreturn { SECTIONS, LEVELS, T, LANES, STAGES, KINDS, RES, LC: typeof LC === \"undefined\" ? {} : LC };")();

let CARDS = {}, MCQS = {};
try { const d = JSON.parse(fs.readFileSync(path.join(root, "flashcards.json"), "utf8")); CARDS = d.topics || {}; MCQS = d.mcq || {}; } catch (e) {}
const cardCount = id => (CARDS[String(id)] || []).length;
const mcqCount = id => (MCQS[String(id)] || []).length;
let TASKS = {};
try { TASKS = JSON.parse(fs.readFileSync(path.join(root, "practice", "tasks.json"), "utf8")).topics || {}; } catch (e) {}
const taskCount = id => (TASKS[String(id)] || []).length;
let LESSONS = {};
try { LESSONS = JSON.parse(fs.readFileSync(path.join(root, "lessons", "index.json"), "utf8")).topics || {}; } catch (e) {}
const lessonTopics = Object.keys(LESSONS).sort((a, b) => a - b);
const totalTasks = Object.values(TASKS).reduce((s, c) => s + c.length, 0);
const taskTopics = Object.keys(TASKS).filter(k => TASKS[k].length).sort((a, b) => a - b);
const totalCards = Object.values(CARDS).reduce((s, c) => s + c.length, 0);
const totalMcqs = Object.values(MCQS).reduce((s, c) => s + c.length, 0);
const cardTopics = [...new Set([...Object.keys(CARDS).filter(k => CARDS[k].length), ...Object.keys(MCQS).filter(k => MCQS[k].length)])].sort((a, b) => a - b);

const topics = T.map(([id, sec, title, level, stage, lane, check, subs]) => ({ id, sec, title, level, stage, lane, check, subs }));
const byId = new Map(topics.map(t => [t.id, t]));
const name = id => `${id} ${byId.get(id).title}`;
const count = l => topics.filter(t => t.level === l).length;

const out = [];
out.push(`${MARKER} (generated from the app's data, do not edit by hand)`);
out.push("");
out.push(`Totals: ${topics.length} topics in ${SECTIONS.length} sections, ${STAGES.length} stages, ${RES.length} resources. ` +
  `Levels: ${count("code")} Coding, ${count("concept")} Concept, ${count("mcq")} MCQ. ` +
  `Flashcards: ${totalCards}, MCQs: ${totalMcqs}${cardTopics.length ? (cardTopics.length === 1 ? " (topic " : " (topics ") + cardTopics.join(", ") + ")" : ""}. ` +
  `Coding tasks: ${totalTasks}${taskTopics.length ? (taskTopics.length === 1 ? " (topic " : " (topics ") + taskTopics.join(", ") + ")" : ""}. ` +
  `Lesson notes: ${lessonTopics.length}${lessonTopics.length ? (lessonTopics.length === 1 ? " (topic " : " (topics ") + lessonTopics.join(", ") + ")" : ""}. ` +
  `LeetCode problems: ${Object.values(LC).reduce((n, l) => n + l.length, 0)}${Object.keys(LC).length ? " (topics " + Object.keys(LC).sort((a, b) => a - b).join(", ") + ")" : ""}.`);
out.push("");
out.push("### Levels");
for (const v of Object.values(LEVELS)) out.push(`- **${v.label}**: ${v.short}`);
out.push("");
out.push("### Lanes (studied side by side inside each stage)");
for (const [, label, desc] of LANES) out.push(`- **${label}**: ${desc}`);
out.push("- Topic 69 (aptitude) runs every day from the start. Topic 71 (frontend) is optional.");
out.push("");
out.push("### Stages");
out.push("Move to the next stage only when its \"Move on when\" check is true. There is no fixed number of days.");
out.push("");
for (const s of STAGES) {
  out.push(`**Stage ${s.n}: ${s.name}**`);
  out.push(`- Core: ${s.core.map(name).join(", ")}`);
  out.push(`- Coding: ${s.coding.length ? s.coding.map(name).join(", ") : s.codingNote}`);
  out.push(`- Light: ${s.light.length ? s.light.map(name).join(", ") : "none"}`);
  out.push(`- Build: ${s.build.length ? s.build.map(name).join(", ") + ". " : ""}${s.buildNote}`);
  out.push(`- Move on when: ${s.gate}`);
  out.push("");
}
out.push("### All topics");
out.push("Format: **id. title** [level, where]. Check = what he must be able to do. Subtopic numbers start at 0 and match the progress backup keys.");
out.push("");
for (const [sec, sname] of SECTIONS) {
  out.push(`#### ${sec}. ${sname}`);
  for (const t of topics.filter(x => x.sec === sec)) {
    const where = t.stage === "Daily" ? "every day" : t.stage === "Optional" ? "optional" : `stage ${t.stage}, ${t.lane} lane`;
    const cards = (LESSONS[String(t.id)] ? ", lesson notes" : "") + (cardCount(t.id) ? `, ${cardCount(t.id)} flashcards` : "") + (mcqCount(t.id) ? `, ${mcqCount(t.id)} MCQs` : "") + (taskCount(t.id) ? `, ${taskCount(t.id)} coding tasks` : "");
    out.push(`- **${t.id}. ${t.title}** [${LEVELS[t.level].label}, ${where}${cards}]`);
    out.push(`  - Check: ${t.check}`);
    out.push(`  - Subtopics: ${t.subs.map((s, i) => `(${i}) ${s}`).join("; ")}`);
    if ((LC[t.id] || []).length) out.push(`  - LeetCode (backup key = number): ${LC[t.id].map(([n, , title, d]) => `${n} ${title} (${d})`).join("; ")}`);
  }
  out.push("");
}
out.push("### Resources");
out.push("All links were opened and checked on 5 Nov 2026. \"Topics\" lists the topic ids each one covers.");
out.push("");
for (const [k, label] of Object.entries(KINDS)) {
  out.push(`#### ${label}`);
  for (const [n, url, , note, ids] of RES.filter(r => r[2] === k)) out.push(`- [${n}](${url}): ${note} Topics: ${ids.join(", ")}.`);
  out.push("");
}

const md = fs.readFileSync(mdPath, "utf8");
const cut = md.indexOf(MARKER);
const head = (cut < 0 ? md : md.slice(0, cut)).replace(/\s+$/, "");
fs.writeFileSync(mdPath, head + "\n\n" + out.join("\n").replace(/\n+$/, "") + "\n");
console.log(`Updated CLAUDE.md: ${topics.length} topics, ${RES.length} resources`);
