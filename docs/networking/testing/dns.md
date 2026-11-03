
# DNS (Domain Name System)

DNS translates domain names into IP addresses, allowing devices to locate services on a network.

## How it works

When a user accesses `example.com`, the resolver looks up the corresponding IP address.

A simplified lookup process:

1. Check the local DNS cache.
2. Query a recursive resolver.
3. If necessary, query the root DNS server.
4. Locate the authoritative nameserver.
5. Return the IP address.

## Common record types

| Record | Purpose |
|---|---|
| A | Maps a domain to an IPv4 address |
| AAAA | Maps a domain to an IPv6 address |
| CNAME | Creates an alias for another domain |
| MX | Specifies mail servers |
| NS | Identifies authoritative nameservers |
| TXT | Stores text-based information |

## Useful commands

Check the IP address associated with a domain:

```bash
dig example.com
```

Query a specific record:

```bash
dig example.com A
```

Check the nameservers:

```bash
dig example.com NS
```

Alternative:

```bash
nslookup example.com
```

## Important ports

| Protocol | Port |
|---|---:|
| DNS (UDP) | 53 |
| DNS (TCP) | 53 |

!!! note "Remember"
    DNS usually uses UDP port 53, but TCP is also used in specific situations, such as zone transfers and responses requiring TCP.

## References

- [RFC 1034 — Domain Names](https://datatracker.ietf.org/doc/html/rfc1034)
- [RFC 1035 — Domain Names: Implementation and Specification](https://datatracker.ietf.org/doc/html/rfc1035)

