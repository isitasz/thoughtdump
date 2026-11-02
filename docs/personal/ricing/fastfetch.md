# fastfetch — customizing

## changing the title

by default, fastfetch utilizes the module `title` to show the users name and the machines hostname.
however, im too lazy to migrate my user to the one i actually like, so i just put a mask on everything to hide it.

just add a format section and put whatever you want there.

```jsonc
{
    "type": "title",
    "format": "user@hostname"
}
```

## changing colors

example: purple and cyan.

```jsonc
{
    "type": "title",
    "format": "{#magenta}scythe{#}@{#cyan}my-system{#}"
}
```

- `{#color}`: self explanatory
- `{#}`: back to original color

## spacing

maybe i just don't know how, but i could only use padding on the logo.

to deslocate the info block i just add `break` modules at the top.

```jsonc
"modules": [
    "break",
    "break",
    // rest of stuff
]
```

or add a format section to add some spaces (if it's horizontally). yes you need to do it to every single module...

```jsonc
{
    "type": "os",
    "format": "  {2}"
}
```

mental reminder to look deeper for a better solution.

## lost the config

no you didn't you just forgot. 

```bash
~/.config/fastfetch/config.jsonc
```

## official documentation

https://github.com/fastfetch-cli/fastfetch
