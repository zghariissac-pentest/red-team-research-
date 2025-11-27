# C2 overview

Command and control is the communication layer between deployed payloads and the operator. A well designed C2 framework ensures reliable communication, controlled execution, and minimal detection. Understanding C2 principles is essential for building secure and effective red team infrastructure.

## Purpose of C2

The goal of a C2 system is to manage compromised hosts, execute commands, transfer data, and maintain persistence. It provides the operator with real time visibility and control over the environment. A stable C2 channel ensures continuity even in restricted network conditions.

## C2 communication models

C2 systems rely on different communication patterns. The two main models are polling and beaconing. In polling, the agent requests instructions at fixed intervals. In beaconing, the agent sends a signal periodically to check for tasks. Both models aim to minimize detection by blending with normal traffic.

## Transport protocols

C2 traffic can use multiple transport options. HTTP and HTTPS are the most common due to their widespread use and ability to blend in. DNS is used in highly restricted environments but provides lower bandwidth. Custom TCP transports offer flexibility but may generate anomalies if not configured properly.

## Callback behavior

The frequency and jitter of callbacks affect how detectable the agent becomes. Longer intervals reduce noise and lower detection. Jitter introduces randomness, preventing defenders from predicting traffic patterns. A good C2 configuration adjusts these values according to the operation type.

## Encryption and encoding

C2 channels must use encrypted communication to prevent inspection. Transport layer encryption ensures confidentiality. Payloads often apply additional encoding or encryption layers inside the traffic. This helps avoid signature based detection and makes decoding difficult for defenders.

## Infrastructure design

A C2 system typically consists of a core server and one or more redirectors. Redirectors handle public exposure and forward traffic. The core server processes tasks and stores results. This separation protects the main C2 from scans and direct attacks.

## Traffic shaping

Blending C2 traffic with legitimate patterns reduces detection. Using common headers, realistic user agents, and normal looking URLs helps the channel appear benign. Some frameworks support profile customization to mimic real applications or web services.

## Operational safety

Never expose the C2 server directly to the internet. Use dedicated domains, redirectors, and isolated VPS instances. Disable unnecessary modules and limit logging. Always test profiles and communication patterns in a controlled environment before using them in an operation.

## Cleanup and rotation

After each engagement, destroy the C2 server, wipe the redirectors, and remove domains. Never reuse old infrastructure. Rotating assets prevents correlation between separate operations and maintains long term safety
