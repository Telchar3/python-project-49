install:
	poetry install

brain-games:
	poetry run brain-games

brain-even:
	poetry run brain-even

brain-calc:
	poetry run brain-calc

brain-progression:
	poetry run brain-progression

brain-prime:
	poetry run brain-prime

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

.PHONY: lint install brain-games build publish package-install
