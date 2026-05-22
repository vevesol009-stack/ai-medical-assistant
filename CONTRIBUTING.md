# Contributing to AI Medical Diagnosis Assistant

Thank you for your interest in contributing! This document provides guidelines for contributing to the project.

## 🌟 Ways to Contribute

- **Bug Reports**: Report bugs via GitHub Issues
- **Feature Requests**: Suggest new features or improvements
- **Code Contributions**: Submit pull requests for bug fixes or features
- **Documentation**: Improve documentation and examples
- **Testing**: Write tests and improve test coverage
- **Translations**: Add support for new languages

## 🚀 Getting Started

### 1. Fork the Repository

Click the "Fork" button at the top right of the repository page.

### 2. Clone Your Fork

```bash
git clone https://github.com/YOUR_USERNAME/ai-medical-assistant.git
cd ai-medical-assistant
```

### 3. Set Up Development Environment

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Install pre-commit hooks
pre-commit install
```

### 4. Create a Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

## 💻 Development Guidelines

### Code Style

- Follow PEP 8 for Python code
- Use Black for code formatting
- Use type hints for function signatures
- Write docstrings for all public functions

```python
def diagnose_symptoms(symptoms: List[str], patient_age: int) -> DiagnosisResult:
    """
    Analyze patient symptoms and return diagnosis.
    
    Args:
        symptoms: List of symptom descriptions
        patient_age: Patient age in years
        
    Returns:
        DiagnosisResult with confidence scores and recommendations
    """
    pass
```

### Testing

- Write unit tests for all new features
- Maintain >90% test coverage
- Run tests before submitting PR

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=app --cov-report=html

# Run specific test file
pytest tests/test_diagnosis.py
```

### Commit Messages

Follow conventional commits format:

```
feat: add voice input support
fix: resolve diagnosis accuracy issue
docs: update API documentation
test: add tests for symptom analysis
refactor: improve database query performance
```

## 🔍 Pull Request Process

1. **Update Documentation**: Update README.md if needed
2. **Add Tests**: Ensure new code has test coverage
3. **Run Linters**: `black app/ && flake8 app/ && mypy app/`
4. **Update Changelog**: Add entry to CHANGELOG.md
5. **Submit PR**: Create pull request with clear description

### PR Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
- [ ] Unit tests added/updated
- [ ] Integration tests added/updated
- [ ] Manual testing completed

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] Tests pass locally
```

## 🏥 Medical Safety Guidelines

**CRITICAL**: This is a medical application. All contributions must prioritize patient safety.

### Required for Medical Features

1. **Medical Validation**: Consult with licensed physicians
2. **Evidence-Based**: Reference medical literature
3. **Disclaimer**: Include appropriate medical disclaimers
4. **Testing**: Extensive testing with real-world scenarios
5. **Review**: Medical professional review before merge

### Prohibited

- ❌ Unvalidated medical advice
- ❌ Diagnosis without confidence scores
- ❌ Treatment recommendations without alternatives
- ❌ Bypassing human-in-the-loop for critical cases

## 📝 Documentation

- Update API documentation for new endpoints
- Add inline comments for complex logic
- Update user guides for new features
- Include examples in docstrings

## 🐛 Bug Reports

Use this template for bug reports:

```markdown
**Describe the bug**
Clear description of the bug

**To Reproduce**
Steps to reproduce:
1. Go to '...'
2. Click on '...'
3. See error

**Expected behavior**
What should happen

**Screenshots**
If applicable

**Environment**
- OS: [e.g. Ubuntu 22.04]
- Python version: [e.g. 3.9.7]
- Browser: [e.g. Chrome 120]
```

## 💡 Feature Requests

Use this template:

```markdown
**Problem Statement**
What problem does this solve?

**Proposed Solution**
How should it work?

**Alternatives Considered**
Other approaches you've thought about

**Additional Context**
Any other relevant information
```

## 🌍 Translation Guidelines

To add a new language:

1. Copy `locales/en.json` to `locales/YOUR_LANG.json`
2. Translate all strings
3. Test with native speakers
4. Ensure medical terminology is accurate

## 📧 Contact

Questions? Reach out:
- Email: taikrhino@gmail.com
- GitHub Issues: For technical questions

## 🙏 Thank You!

Every contribution helps make healthcare more accessible. Thank you for being part of this mission!
