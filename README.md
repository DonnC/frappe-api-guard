### FAG

Frappe Api Guard - control api endpoints access

This project came to light due to the need to control rest api endpoint access.

In frappe, anyone can access the endpoints of any app or doctype, I wanted a way to control what is exposed to the calling clients.

![pic](shot.png)

### Installation

You can install this app using the [bench](https://github.com/frappe/bench) CLI:

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app https://github.com/DonnC/fag.git --branch develop
bench install-app fag
```

### Contributing

This app uses `pre-commit` for code formatting and linting. Please [install pre-commit](https://pre-commit.com/#installation) and enable it for this repository:

```bash
cd apps/fag
pre-commit install
```

Pre-commit is configured to use the following tools for checking and formatting your code:

- ruff
- eslint
- prettier
- pyupgrade

### License

mit
