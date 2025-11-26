# Evading Antivirus

Traditional antivirus focuses on scanning files, monitoring process behavior, and detecting known malicious patterns. While EDR solutions analyze deep system activity, antivirus engines still play a key role in blocking suspicious binaries, scripts, and payloads. Evading antivirus requires removing predictable indicators, reducing static signatures, and controlling execution flow to avoid triggering heuristic engines.

## Understanding Antivirus Detection

Antivirus engines rely on several layers. Static analysis examines the binary structure, strings, imports, and embedded patterns. Heuristic engines simulate execution to detect suspicious behavior. Cloud based reputation systems analyze file metadata, age, and origin. To evade these layers, the payload must appear unique, minimal, and free of known malicious characteristics.

## Reducing Static Signatures

Static signatures are created from recognizable byte patterns, imported functions, or strings commonly found in malicious tools. To avoid detection, the binary must be transformed so that no known signature remains. Packing, custom encryption, or rewriting portions of the code can help remove predictable patterns.

Avoid embedding obvious strings, function names, or configuration data in plaintext. Compressing or encoding sensitive content forces antivirus engines to rely more on behavior, which can be controlled more easily.

## Controlling Heuristic Triggers

Heuristic engines evaluate how the file behaves when executed. Actions such as creating new processes, writing to sensitive directories, or injecting code into other processes create strong detection signals. To bypass these triggers, the payload should perform only necessary actions and avoid aggressive behavior.

Delaying sensitive actions, imitating normal program flow, or using indirect execution pathways helps reduce the number of behaviors flagged as suspicious. The goal is to make the payload look like a legitimate application.

## Custom Compilers and Toolchains

Using publicly known offensive tools often leads to quick detection because antivirus engines store signatures for their output. Building payloads from custom toolchains or compiling source code with different settings creates unique binaries that do not match known patterns.

Modifying compiler flags, altering code structure, and introducing slight variations in function layout all contribute to reducing static detectability. Each build becomes unique, reducing the chance of signature based detection.

## Obfuscation and Encryption

Obfuscating the code makes it harder for antivirus engines to analyze the payload. Techniques include encrypting the main logic, using runtime decryption, or breaking code into smaller segments that execute only when needed.

Obfuscation should be lightweight. Excessive layers make the payload look suspicious and can trigger heuristic rules. Balanced obfuscation protects the payload while maintaining normal behavior.

## Script Based Evasion

Script files such as PowerShell or JavaScript are often scanned before execution. To bypass detection, operators should avoid common malicious commands, minimize the script’s footprint, and use dynamic execution techniques.

Embedding logic in encoded strings, downloading components at runtime, or using native APIs indirectly helps reduce the visibility of the script. Each line should appear harmless when read statically.

## Avoiding Reputation Based Blocking

Files with low reputation or new binaries downloaded from the internet are often flagged automatically. To avoid this, payloads should not appear as newly created or suspicious files. Hosting files internally, avoiding external download links, and minimizing distribution improves reputation compliance.

Where possible, payloads should not be provided as standalone executable files. Running code in memory or using trusted system tools reduces dependence on file based execution.

## Blending with Normal Activity

Antivirus products compare behavior to legitimate patterns. Running payloads at unexpected times, performing unusual actions, or modifying restricted areas increases the chance of detection. To bypass these checks, mimic common user or administrator behavior and perform actions gradually.

Keeping resource usage low, avoiding spikes in network activity, and limiting changes to the system all help maintain stealth. The goal is to appear as a normal, low risk application.

## Continuous Adjustment

Antivirus engines update frequently. A technique that bypasses detection today may not work tomorrow. Operators must constantly adjust payloads, update their build processes, and test against multiple engines to maintain evasion capabilities.

Version rotation, custom builds, and using multiple obfuscation strategies ensure long term success and reduce the risk of predictable patterns being detected
