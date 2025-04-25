# Self-Thinking Data Manifest (STDM)

STDM enables data artifacts, including documents, to guide their own interpretation by Large Language Models (LLMs), creating interactive, self-directing experiences that preserve author intent while unlocking new analytical capabilities.

# Note: The v0.1 specification details an experimental concept. Its safe implementation relies heavily on the security principles outlined within it (esp. Sec 6.0, 7.1, 7.6) and requires careful consideration by implementers. This repository is intended for discussion and research. 

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

## ⚠️ Note of Caution

STDM is an experimental framework still in early development. While it aims to enhance data utility and preserve author intent, it involves directing LLM behavior which carries inherent risks, including causing unexpected behaviour. The specification incorporates mitigation strategies, but users should approach implementation with appropriate caution and security considerations.

## Development

The HTML version of the specification is built from the markdown source:

```
python build/build.py stdm_spec_v0.1.md instructions.txt template.html index.html
```

## Contributing

We welcome feedback, examples, and contributions to help evolve this specification into a robust standard for LLM-data interaction.
