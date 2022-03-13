# filego

* Simple yet powerful file organising tool.
* Fully dynamic, where user can define multiple extensions to include.
* Use file_path_defination.json as a input.
* Input Instructions -

``` json
{
    "source_path": "Directory path from where you want to perform the moving process",
    "destination_path": {
        "lable": {
            "path": "Directory path for that label",
            "extensions": [
                "List of extensions that you want to include in above path",
                "like this [.mp4,.mkv]",
                "Dont forget to include (.) before the extension",
                "You can add multiple labels"
            ]
        },
        "Pictures": {
            "path": "directory path",
            "extensions": [
                ".png",
                ".jpg",
                ".jpeg"
            ]
        }

    }
}
```
