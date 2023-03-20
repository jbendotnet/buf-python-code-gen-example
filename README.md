# Buf Python Code-gen Example

NB: App layout assumes Poetry used for dependency management etc

```shell
poetry run python buf_python_code_gen_example/main.py
```

Expected output:

```
2023-03-20 09:35:43 [info     ] Download request:              request=url: "https://picsum.photos/200/300"

2023-03-20 09:35:43 [info     ] Download response:             response=file {
  name: "image.jpg"
}
```