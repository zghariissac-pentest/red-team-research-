# VPN and Proxy Setup

VPNs and proxies are essential components of red team operational security. They hide the operator’s real IP, mask geolocation, and provide a controlled network path to infrastructure. Without proper setup, even the most careful operation can be traced back to the operator.

The goal is to use VPNs and proxies consistently, compartmentalized per operation, and configured to minimize leaks and identifiable patterns.

## Choosing a VPN

When selecting a VPN, choose providers with strong privacy policies, minimal logging, and anonymous payment options. Avoid free VPN services or providers that require personal information, as they are often monitored or could expose identity.

Consider VPNs that allow connection from multiple devices, provide stable bandwidth, and support different protocols. Multi-hop VPNs can add an extra layer of anonymity but must be used carefully to avoid introducing latency that disrupts operations.

## Proxy Use

Proxies can be used to separate specific operational traffic from other VPN connections. They provide another layer of compartmentalization and can help rotate identities per task. HTTP, SOCKS5, and residential proxies have different characteristics and use cases.

Use proxies to access target infrastructure, deliver payloads, or perform reconnaissance without revealing your main IP. Rotate proxies regularly to avoid patterns and detection.

## Combining VPN and Proxy

For optimal OPSEC, combine VPN and proxy in layered configurations. For example, the operator connects to a VPN, then routes traffic through a proxy to operational servers. This ensures that the original IP is hidden at multiple levels.

Ensure that DNS and WebRTC leaks are disabled. Test connections regularly to confirm the true IP is not exposed. Even small leaks can compromise anonymity.

## Compartmentalization

Every engagement requires separate network paths. Do not reuse the same VPN account or proxy IP across multiple operations. Each project should have dedicated VPN and proxy resources.

Compartmentalization prevents correlation attacks and reduces the risk of attribution. If one IP is discovered, it should not compromise other operations.

## Operational Hygiene

Do not connect to personal accounts or browse personal content while using operational VPNs and proxies. Every action taken on these networks should align with operational personas.

Keep configuration consistent. Avoid software updates or other activities that can change network fingerprints. Document VPN and proxy details internally for rotation and troubleshooting, but never link this documentation to personal information.

## Testing and Verification

Before using a VPN or proxy in an operation, test it for leaks, latency, and stability. Verify that traffic is routed correctly and no metadata is exposed. Periodically re-test configurations to ensure ongoing reliability
