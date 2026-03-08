## Bad

```python
s = ""
for item in items:
    s += item
```

## Better

```python
parts = []
for item in items:
    parts.append(item)
s = "".join(parts)
```
