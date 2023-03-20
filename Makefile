buf/generate:
	@docker run --rm -it \
    -v ${PWD}:/workspace \
    --workdir /workspace \
    bufbuild/buf:latest \
    generate --include-imports --debug -v

buf/modupdate:
	@docker run --rm -it \
    -v ${PWD}:/workspace \
    --workdir /workspace \
    bufbuild/buf:latest \
    mod update proto --debug

buf/lint:
	@docker run --rm -it \
    -v ${PWD}:/workspace \
    --workdir /workspace \
    bufbuild/buf:latest \
    lint --debug

buf/format:
	@docker run --rm -it \
    -v ${PWD}:/workspace \
    --workdir /workspace \
    bufbuild/buf:latest \
    format -w -d

buf/breaking:
	@docker run --rm -it \
    -v ${PWD}:/workspace \
    --workdir /workspace \
    bufbuild/buf:latest \
    breaking --exclude-imports --against 'https://github.com/jbendotnet/python-codegen-buf-problem.git#branch=main' --debug
