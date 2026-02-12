/**
 * Background service worker — Manifest V3
 *
 * Runs in the extension's background context.
 * Use this for event listeners, alarms, and API proxying.
 */

chrome.runtime.onInstalled.addListener(() => {
    console.log("Job Hunter AI CRM extension installed ✅");
});
