from setuptools import find_packages, setup

GITHUB_URL = "https://github.com/tfiers/githyperlink"

with open("ReadMe.md", mode="r", encoding="utf-8") as f:
    readme = f.read()

setup(
    name="githyperlink",
    author="Tomas Fiers",
    author_email="tomas.fiers@gmail.com",
    long_description=readme,
    long_description_content_type="text/markdown",
    url=GITHUB_URL,
    project_urls={"Source Code": GITHUB_URL},
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">= 3.9",  # We use `removesuffix`, so 3.9 minimum.
    install_requires=[
        "click >= 6",
        # `click`'s major version goes up relatively fast, and it's never really
        # breaking. Hence the `>` instead of `~`.
        # `v6.0` is from end 2015 (a bit over 6 years ago at the time of writing).
    ],
    packages=find_packages("src"),
    package_dir={"": "src"},  # (`""` is the "root" package).
    entry_points={
        "console_scripts": [
            "gethyperlink = githyperlink.cli:get_and_print_hyperlink"
        ]
    },
    # Get package version from git tags
    setup_requires=["setuptools_scm"],
    use_scm_version={
        "version_scheme": "post-release",
        "local_scheme": "dirty-tag",
    },
)
