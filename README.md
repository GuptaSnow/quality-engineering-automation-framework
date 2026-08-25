# quality-engineering-automation-framework

A Python-based test automation framework demonstrating scalable Quality
Engineering practices across API and web UI automation.

The framework is designed with maintainability, test isolation,
reusability, and clear separation of responsibilities in mind.

## Technology Stack

- Python 3.11+
- Pytest
- Requests
- Playwright
- pytest-playwright
- Pydantic
- pytest-xdist
- pytest-html
- python-dotenv
- Ruff
- Black
- GitHub Actions

## Current Capabilities

### API Automation

The API layer currently demonstrates:

- Reusable HTTP client
- Domain-specific API service layer
- Pytest fixtures
- Pydantic response validation
- Email format validation
- Positive testing
- Negative testing
- Parameterized tests
- Expected-failure handling

Current API operations include:

- Get user
- Create user
- Update user
- Delete user

### Web Automation

The web automation layer uses Playwright and is structured around:

- Browser lifecycle management
- Browser context isolation
- Page fixtures
- Page Object Model
- Separate UI test data
- Positive and negative login scenarios

## Architecture

```text
                         Pytest
                           |
              +------------+------------+
              |                         |
             API                       WEB
              |                         |
         API Client                Playwright
              |                         |
         Users API                Page Objects
              |                         |
         Pydantic                 Browser
          Schemas                 Context
              |                         |
              +------------+------------+
                           |
                        Fixtures
                           |
                       Test Data
                           |
                    Tests / Validation
