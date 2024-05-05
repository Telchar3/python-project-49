install:
	poetry install

brain-games:
	poetry run brain-games
	poetry run brain-even

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-reinstall:
	python3 -m pip install --user dist/*.whl --force

lint:
	poetry run flake8 brain_games

.PHONY: install brain-games build publish package-install
