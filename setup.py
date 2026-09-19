from setuptools import setup

setup(
    name="my_saas_app",
    version="0.0.1",
    description="A SaaS application built on Frappe",
    author="Frappe",
    author_email="hello@example.com",
    packages=["my_saas_app"],
    zip_safe=False,
    include_package_data=True,
)
