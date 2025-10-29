// setup_tags.js
// Automate creation of GitHub issue labels for TigerByte repo

import fetch from "node-fetch";

// 🟢 Replace with your repo details
const GITHUB_TOKEN = "YOUR_GITHUB_TOKEN_HERE";
const OWNER = "YourGitHubUsername";
const REPO = "TigerByte";

const headers = {
  "Authorization": `token ${GITHUB_TOKEN}`,
  "Accept": "application/vnd.github+json",
  "Content-Type": "application/json",
};

// 🏷️ Tag definitions (based on tagging-system.md)
const tags = [
  // 🟦 Status Tags
  { name: "In Progress", color: "0d6efd", description: "Task is currently being worked on." },
  { name: "Completed", color: "198754", description: "Work is done and merged." },
  { name: "Review Needed", color: "ffc107", description: "Awaiting review." },
  { name: "Needs Info", color: "e4e669", description: "Waiting for contributor response." },
  { name: "Stale", color: "adb5bd", description: "No recent activity; may be closed soon." },

  // 🔴 Priority Tags
  { name: "High Priority", color: "dc3545", description: "Immediate attention required." },
  { name: "Medium Priority", color: "fd7e14", description: "Should be addressed soon." },
  { name: "Low Priority", color: "20c997", description: "Can be done when time permits." },

  // 🧠 Type of Issue Tags
  { name: "Bug", color: "f87171", description: "Code errors or malfunctions." },
  { name: "Feature Request", color: "c084fc", description: "Suggestion for a new feature." },
  { name: "Documentation", color: "60a5fa", description: "Docs or guides." },
  { name: "Refactor", color: "fbbf24", description: "Code cleanup or optimization." },
  { name: "UI/UX", color: "f472b6", description: "User interface or experience improvements." },
  { name: "Testing", color: "38bdf8", description: "Tests or QA tasks." },

  // 🧱 Area/Component Tags
  { name: "Frontend", color: "fde68a", description: "Frontend-related work." },
  { name: "Backend", color: "99f6e4", description: "Backend logic or APIs." },
  { name: "Database", color: "a7f3d0", description: "Database models or queries." },
  { name: "DevOps", color: "d9f99d", description: "CI/CD, Docker, or deployment." },
  { name: "Security", color: "fca5a5", description: "Security-related tasks." },

  // 🙌 Contributor-Focused
  { name: "Good First Issue", color: "86efac", description: "Beginner-friendly task." },
  { name: "Help Wanted", color: "3b82f6", description: "Needs community support." },
  { name: "Under Review", color: "eab308", description: "Awaiting maintainer feedback." },
  { name: "Assigned", color: "f59e0b", description: "Assigned to a contributor." },

  // 🐯 TigerByte-Specific
  { name: "#TigerByteGoals", color: "facc15", description: "Major project milestones." },
  { name: "#ByteSquad", color: "a855f7", description: "Collaborative team tasks." },
  { name: "#ByteMe", color: "ef4444", description: "Fun or experimental issues." },
  { name: "#CodeRoar", color: "22d3ee", description: "Performance or optimization tasks." },
  { name: "#TigerTales", color: "f97316", description: "Docs or storytelling updates." },
  { name: "#PawPrints", color: "84cc16", description: "UI/UX design enhancements." },
  { name: "#TigerFix", color: "fb7185", description: "Quick critical fixes." },

  // 🎉 Seasonal/Event
  { name: "#Hacktoberfest2025", color: "ff6f00", description: "Hacktoberfest-related contributions." },
  { name: "#Christmas2025", color: "16a34a", description: "Holiday-themed updates." },
  { name: "#NewYearSprint2026", color: "60a5fa", description: "New Year cleanups." },
  { name: "#SummerOfCode2026", color: "fbbf24", description: "Internship or GSoC tasks." },
];

// 🧹 Step 1: Delete all old labels (optional cleanup)
async function deleteOldLabels() {
  const res = await fetch(`https://api.github.com/repos/${OWNER}/${REPO}/labels`, { headers });
  const labels = await res.json();
  for (const label of labels) {
    await fetch(`https://api.github.com/repos/${OWNER}/${REPO}/labels/${encodeURIComponent(label.name)}`, {
      method: "DELETE",
      headers,
    });
    console.log(`🗑️ Deleted old label: ${label.name}`);
  }
}

// 🏗️ Step 2: Create all new tags
async function createLabels() {
  for (const tag of tags) {
    const res = await fetch(`https://api.github.com/repos/${OWNER}/${REPO}/labels`, {
      method: "POST",
      headers,
      body: JSON.stringify(tag),
    });
    if (res.ok) {
      console.log(`✅ Created label: ${tag.name}`);
    } else {
      console.error(`⚠️ Failed to create: ${tag.name}`, await res.text());
    }
  }
}

// 🚀 Main Function
(async () => {
  console.log("🧹 Cleaning up old labels...");
  await deleteOldLabels();

  console.log("\n🏗️ Creating new TigerByte label system...");
  await createLabels();

  console.log("\n🎉 Tagging system setup complete!");
})();
