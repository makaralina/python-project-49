install:
	@poetry install

build:
	@poetry build

publish:
	@poetry publish --dry-run

package-install:
	@python3 -m pip install dist/*.whl

lint:
	@poetry run flake8 brain_games

brain-games:
	@poetry run brain-games

brain-even:
	@poetry run brain-even

.PHONY: install build publish package-install lint  brain-games brain-even