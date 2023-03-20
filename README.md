# Buf Python Code-gen Example

NB: App layout assumes Poetry used for dependency management etc

```shell
poetry run python app/main.py
```

Expected output:

```
2023-03-20 09:35:43 [info     ] Download request:              request=url: "https://picsum.photos/200/300"

2023-03-20 09:35:43 [info     ] Download response:             response=file {
  name: "image.jpg"
}
```

## Updating protos

If you update the protos, simply run `buf generate` in the root of the repo re-generate them.
