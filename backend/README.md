## How to run:
### Docker
1. `docker compose up`
### Native
1. Add env params form `app/settings.py`
2. poetry install
3. litestar run

## Structure
```
  app
├── api          - Controllers from MVC
│   └── ...
├── models       - Neural models interfaces and implementations
│   └── ...
├── services     - Business logic
│   └── ...
├── storage      - Database relatet stuff
│   └── ...
├── utils        - Extra features for QoL e.g. dependencie injections
│   └── ...
├── app.py       - App root
├── schemas.py   - Api validation schemas
├── state.py     - Vauilt with instances/generators for DI
└── settings.py  - Automatic env validation
```
