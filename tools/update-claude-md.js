// Regenerates section 7 of CLAUDE.md (the roadmap reference) from the data inside index.html,
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
const { SECTIONS, LEVELS, T, LANES, STAGES, KINDS, RES } =
  new Function(html.slice(start, end) + "\nreturn { SECTIONS, LEVELS, T, LANES, STAGES, KINDS, RES };")();

const topics = T.map(([id, sec, title, level, stage, lane, check, subs]) => ({ id, sec, title, level, stage, lane, check, subs }));
const byId = new Map(topics.map(t => [t.id, t]));
const name = id => `${id} ${byId.get(id).title}`;
const count = l => topics.filter(t => t.level === l).length;

const out = [];
out.push(`${MARKER} (generated from the app's data, do not edit by hand)`);
out.push("");
out.push(`Totals: ${topics.length} topics in ${SECTIONS.length} sections, ${STAGES.length} stages, ${RES.length} resources. ` +
  `Levels: ${count("code")} Coding, ${count("concept")} Concept, ${count("mcq")} MCQ.`);
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
    out.push(`- **${t.id}. ${t.title}** [${LEVELS[t.level].label}, ${where}]`);
    out.push(`  - Check: ${t.check}`);
    out.push(`  - Subtopics: ${t.subs.map((s, i) => `(${i}) ${s}`).join("; ")}`);
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
