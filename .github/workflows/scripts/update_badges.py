import tomlkit
import re

# Read pyproject.toml
with open('pyproject.toml', 'r') as file:
    pyproject = tomlkit.parse(file.read())

# Extract dependency versions
dependencies = pyproject['tool']['poetry']['dependencies']
python_version = dependencies['python']
beautifulsoup4_version = dependencies['beautifulsoup4']
requests_version = dependencies['requests']

# Read README.md
with open('README.md', 'r') as file:
    readme = file.read()

# Update badges
readme = re.sub(r'python-[^\-]+-blue', f'python-{python_version}-blue', readme)
readme = re.sub(r'beautifulsoup4-[^\-]+-blue', f'beautifulsoup4-{beautifulsoup4_version}-blue', readme)
readme = re.sub(r'requests-[^\-]+-blue', f'requests-{requests_version}-blue', readme)

# Write updated README.md
with open('README.md', 'w') as file:
    file.write(readme)
