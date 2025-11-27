# Redirectors types

Redirectors are lightweight servers that forward traffic between the target and the core command server. They hide the true location of your command and control and help shape, filter, or blend traffic. Good redirector design reduces detection and increases operational safety.

## Purpose of redirectors

Redirectors separate the public facing infrastructure from sensitive backend systems. They absorb scans, handle filtering rules, and forward only legitimate traffic. This improves stealth and adds an additional security layer.

### HTTP redirectors

These redirectors handle web based traffic. They forward HTTP or HTTPS requests to the backend server. They often run simple web servers like Apache or Nginx. They are used when payloads communicate over web protocols or when staging content is hosted through domain fronting or normal HTTPS traffic.

### TCP redirectors

TCP redirectors are used for raw socket traffic such as custom C2 protocols. They forward packets at the TCP level without parsing the data. Tools like socat, rinetd, or iptables rules are commonly used. They are simple, fast, and difficult for defenders to fingerprint.

### Domain fronting redirectors

Domain fronting uses large content delivery networks. The redirector uses a front domain for the TLS handshake while directing traffic to a hidden backend within the same CDN provider. This technique blends traffic with legitimate high reputation domains. It relies on the CDN supporting mismatched hostnames.

### CDN based redirectors

Using CDN services provides an additional layer of anonymity. The redirector does not expose the real server and distributes requests through global edges. This improves evasion and performance. The backend server location stays hidden behind the provider.

### Multi stage redirectors

Multi stage designs use several redirectors chained together. The first layer handles public exposure. The second layer filters traffic. The third layer communicates with the backend. This structure increases resilience and protects the core server even if one redirector is exposed.

### Filtering mechanisms

Redirectors can inspect and filter traffic based on user agent, URI patterns, headers, or packet metadata. This allows dropping unwanted scanners or detections. Traffic shaping also helps emulate normal web behavior and reduce anomalies.

### Operational considerations

Each redirector must be isolated. Avoid reusing IP addresses or domains across campaigns. Limit the amount of logging on redirectors. Always ensure the redirector does not reveal the backend address in error messages, redirects, or headers
