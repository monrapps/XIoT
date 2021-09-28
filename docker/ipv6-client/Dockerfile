FROM ipv6-base

# Copy client application
COPY ipv6-echo-tester ./ipv6-echo-tester

# Copy initialization Script
COPY init ./init

# Configure initialization script as entrypoint
ENTRYPOINT ["./init"]
