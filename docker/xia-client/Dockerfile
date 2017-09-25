FROM xia-base

# Copy client application
COPY xia-echo-tester ./xia-core/applications/example/xia-echo-tester

# Copy initialization Script
COPY init ./init

# Configure initialization script as entrypoint
ENTRYPOINT ["./init"]
