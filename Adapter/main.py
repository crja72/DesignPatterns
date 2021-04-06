class Target:
    def return_dict(self) -> dict:
        return {
            "key1": "val1",
            "key2": "val2"
        }


class ClassToAdapt:
    def return_str(self) -> str:
        return "key1:val1,key2:val2"


class Adapter(Target, ClassToAdapt):
    def return_dict(self) -> dict:
        data = self.return_str().split(',')
        res = {}
        for item in data:
            k, v = item.split(':')
            res[k] = v
        return res


def client_code(target: Target) -> None:
    data = target.return_dict()
    print(data)


if __name__ == "__main__":
    adapter = Adapter()
    client_code(adapter)
