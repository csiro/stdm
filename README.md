# Self-Thinking Data Manifest (STDM)

STDM enables data artifacts, including documents, to guide their own interpretation by Large Language Models (LLMs), creating interactive, self-directing experiences that preserve author intent while unlocking new analytical capabilities.

## ⚠️ Caution

The v0.1 specification details an experimental concept. Implementation requires consideration of the security principles outlined in sections 6.0, 7.1, and 7.6.
STDM is in early development. While it aims to enhance data utility and preserve author intent, it involves directing LLM behavior which carries risks, including causing unexpected behaviour. The specification incorporates mitigation strategies, but the community should apply appropriate caution and security considerations.

## What is STDM?

STDM embeds structured instructions within documents, images, or data files that direct how LLMs should process, analyze, and present the data. This creates "smart artifacts" capable of:

- Rendering interactive interfaces with custom navigation
- Executing data analysis on embedded content
- Creating guided exploration of complex documents
- Providing intelligent assistance tailored to specific data
- Maintaining context and purpose across interactions

## Visual Indicators

**I am Thinking Data Ribbon**: STDM-enabled documents are visually marked with a colorful "I am Thinking Data" ribbon in the top-right corner. This ribbon:
- Provides a clear visual indicator that the document contains STDM instructions
- Helps users identify documents with embedded intelligence
- Can be dismissed by clicking the "×" in the ribbon if desired
- Is included in examples like the floodplain visualization

## Getting Started

- **Specification**: The complete [STDM v0.1 Specification](stdm_spec_v0.1.md) explains the format, structure, and recommended implementation patterns.
- **Live Demo**: View the [rendered specification](index.html) which is itself an experimental STDM document.
- **Examples**: Check the examples directory for implementation samples in various formats.
  - **Floodplain Inundation Study**: [floodplain.html](examples/floodplain.html) - An interactive HTML poster of the open access paper "Floodplain inundation in the Murray–Darling Basin under current and future climate conditions." This example embeds the complete paper and provides STDM instructions that enable LLMs to navigate and analyze the content page by page.


## Development

The HTML version of the specification is built from the markdown source:

```
python build/build.py stdm_spec_v0.1.md instructions.txt template.html index.html
```

## Frequently Asked Questions (FAQ)

**Q1: What exactly is a Self-Thinking Data Manifest (STDM)?**

**A:** A Self-Thinking Data Manifest (STDM) is a digital artifact (like an HTML page, text file, or even metadata within a PDF or image) that bundles primary data content (often text) with explicit, structured instructions. These instructions define how a Large Language Model (LLM), acting as an external interpretation engine, should process, interact with, present, or execute tasks related to the artifact's embedded data.

*   **Core Idea:** The goal is to create self-directing artifacts. Instead of just passive data, an STDM contains a blueprint guiding an LLM on how to provide a specific, predictable, and potentially interactive experience tailored to that data. The term 'Self-Thinking' evocatively refers to the manifest's ability to provide these self-contained directions for the LLM's actions concerning the data. The core principle is: "The manifest directs the engine's 'thought process' and user experience of the data."
*   **Natural Language Programming:** STDM leverages the advanced instruction-following capabilities of modern LLMs. By using structured natural language directives like `GOAL` (the objective), `CONSTRAINTS` (rules/boundaries), `REQUESTED_TOOLS` (needed capabilities), and `CUSTOM_UI_DEFINITION` (presentation/interaction format), authors can effectively "program" the LLM's behaviour for that specific data context. The LLM interprets these high-level instructions much like a computer interprets code.
*   **Inverting "Chat Over Data":** Traditionally, making data interactive with an LLM often involves building a separate application or chat interface *on top of* the data. STDM inverts this model. It embeds the interaction logic, persona, and presentation guidelines *directly within the data artifact itself*. When a user provides this artifact to a compatible LLM interpreter and gives an explicit command to run it, the artifact essentially brings its own custom interface and interaction pattern with it, powered by the LLM.

**Q2: How is STDM different from standard prompt engineering?**

**A:** While both involve providing instructions to an LLM, STDM formalizes and bundles these instructions with data.

*   **Prompt Engineering:** Typically involves a user crafting prompts (often ad-hoc) during an interaction to guide the LLM for the immediate task. The prompt might be separate from the data, ephemeral, and highly dependent on the user's skill in phrasing it.
*   **STDM:** Aims to create *portable, self-contained artifacts* where the *author* embeds structured instructions directly alongside the data. These instructions (using directives like `GOAL`, `CONSTRAINTS`, `CUSTOM_UI_DEFINITION`) provide a consistent, intended interaction pattern or analysis pathway for *anyone* using that specific STDM-enabled artifact with a compatible LLM interpreter. It moves from ad-hoc user prompts to author-defined, data-coupled, reusable guidance.

**Q3: Why is now the right time for a concept like STDM?**

**A:** The emergence of Large Language Models with significantly **larger context windows** is a key enabler.

*   Previously, LLM context windows were often too small to hold both substantial data content *and* detailed processing instructions simultaneously.
*   Modern LLMs can process hundreds of thousands, or even millions, of tokens. This allows an entire document, dataset (in textual form), or complex configuration file to be loaded into the LLM's context *along with* a comprehensive set of STDM instructions (including goals, constraints, UI definitions, and fallback logic).
*   This technical capability makes the core STDM concept – bundling data with its own interpretation guide – practically feasible.

**Q4: Isn't STDM just enabling or facilitating malicious prompt injection?**

**A:** STDM acknowledges the risks associated with LLMs processing external instructions, including malicious prompt injection. It proposes specific mechanisms centered on **user control and explicit intent** to mitigate these risks.

*   **Existing Challenge:** Malicious prompt injection techniques, where hidden instructions attempt to hijack the LLM's behavior or bypass safety measures, are an existing challenge for *all* LLM interactions, independent of STDM. STDM does not introduce new injection vectors nor publicise existing approaches.
*   **STDM Scope & Intent:** The STDM specification (v0.1) does **not** explore, test, or intend methods to override LLM safety protocols or existing prompt injection defenses. Its design aims to operate transparently *within* those safety boundaries, providing *authorized*, task-specific guidance.
*   **Mitigation 1: Explicit User Invocation (Sec 6.0, 7.6):** The core safety principle is that an LLM interpreter should *not* automatically execute an STDM upon detection. The user *must explicitly command* the LLM to process the STDM instructions for the provided artifact (e.g., "Run the STDM in this document"). This signals user trust and intent for *that specific task*, helping the LLM differentiate the STDM instructions (as authorized guidance) from potentially unauthorized or malicious input. The mandatory Safety Preamble reinforces this critical step.
*   **Mitigation 2: Tool Use Consent Gate (Sec 6.1, 7.1):** Even if the user invokes the STDM, any action requiring potentially risky tools (like code execution or web access) requires a *second*, specific, informed consent step from the user before execution. The STDM can only *request* tools; the user *authorizes* their use for the stated purpose.
*   **Mitigation 3: LLM Core Safety:** STDM instructions operate *within* the LLM's existing safety protocols. An STDM should not be able to force an LLM to violate its fundamental safety alignment (e.g., generating harmful content).
*   **Summary:** STDM attempts to manage the inherent risks of instruction-following by structuring the interaction around explicit user commands and consent, aiming for transparent, user-authorized guidance rather than enabling the deceptive execution characteristic of malicious prompt injection. It relies on the LLM's underlying safety features to handle injection attempts, just like any other interaction.

**Q5: How does a user know if a document contains an STDM?**

**A:** This specification (v0.1) focuses on the format and LLM interpretation. Artifacts containing an STDM should be clearly identifiable as such (e.g., via labelling or naming conventions), promoting user awareness before interaction. Additional mechansisms include: 

*   **LLM Interpreter Notification:** Upon receiving a document and an explicit "run" command, the LLM interpreter should ideally notify the user that it has detected STDM instructions and state the `GOAL` before proceeding (as guided by the Safety Preamble).
*   **File Naming/Metadata:** Authors could use naming conventions (e.g., `.stdm.html`) or explicit metadata fields.
*   **Visual Indicators:** Documents could icon or notice indicating the presence of embedded instructions. An example banner is provided.
*   **Transparency Principle (Sec 2.3):** While instructions shouldn't interfere with normal viewing, they should be accessible for review. How this is best implemented in different file types is an area for exploration.

**Q6: What happens if an STDM author has malicious intent (e.g., creates a manipulative UI or misleading GOAL)?**

**A:** If an author embeds instructions with malicious intent – aiming to deceive the user, bypass safety protocols, or execute harmful actions – they are fundamentally not implementing an STDM according to its definition and principles. **This is simply designing a prompt injection attack.**

**Q7: Who builds the "LLM interpreter" for STDM, and how standardized does it need to be?**

**A:** STDM v0.1 is an experimental specification, and its interpretation model deliberately leans on the advanced natural language understanding capabilities of Large Language Models.

*   **The LLM as the Core Interpreter:** The primary "interpretation" of the STDM's natural language directives (`GOAL`, `CONSTRAINTS`, `PERSONA`, etc.) is performed by the **LLM itself**. The power of STDM comes from the LLM's ability to understand context, follow high-level instructions, and reason about the task described, even with the inherent fuzziness of natural language. The STDM structure provides guidance, not rigid code.
*   **Role of the Handling System/Platform:** While the LLM understands the *content* of the directives, the system or platform interacting with the LLM (e.g., a chatbot interface, a document analysis tool, an integrated application) plays a critical role in *handling* the STDM artifact according to the specification's principles. This includes:
    *   Reliably detecting the `[STDM START]`...`[STDM END]` block.
    *   Correctly presenting the STDM instructions and the associated data payload to the LLM within the interaction context.
    *   **Crucially, enforcing the safety protocols:** Checking for explicit user invocation (as prompted by the Safety Preamble) before acting on the `GOAL`, and managing the mandatory user consent process before executing any `REQUESTED_TOOLS`.
    *   Managing the interaction flow based on the `CUSTOM_UI_DEFINITION` and user responses.
*   **Implementation Flexibility:** This handling logic could be implemented by LLM developers directly into their platforms, by researchers building experimental tools, or by third-party application developers integrating LLM APIs. The key is adherence to the *principles* (especially safety and user control) rather than a rigidly standardized low-level parsing engine.
*   **Goal of Portability:** While avoiding over-standardization of the interpretation *logic* (which relies on the LLM), the goal remains that STDM artifacts using the defined structure and directives should be understandable and usable across different LLM systems that *support* the STDM handling principles, particularly the safety mechanisms.

**Q8: What are the limitations of STDM v0.1?**

**A:** As an initial specification, v0.1 has limitations:

*   **Text Focus:** Primarily designed for text-based data payloads due to current LLM strengths (Sec 3.3). Reliably interpreting complex binary data embedded directly is challenging.
*   **Simple Logic:** Lacks sophisticated programming constructs like conditional logic (`if/else`) or persistent state variables defined *within* the STDM itself (though the LLM might maintain conversational state).
*   **Interpreter Dependence:** Effectiveness relies heavily on the LLM's capabilities to understand the instructions and the handling system's adherence to the spec (especially safety protocols like invocation checks and consent gates), and its ability to render UIs or use tools.
*   **Security Reliance:** Security hinges significantly on correct implementation and enforcement of user invocation checks and consent gates by the LLM handling system, and the LLM's own safety foundation.
*   **Standardization:** It's not yet a formal standard, meaning interoperability is not guaranteed.