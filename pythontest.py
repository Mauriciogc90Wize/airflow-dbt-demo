import os
import aiohttp
from git import Repo
from gidgethub import routing, sansio
from gidgethub import aiohttp as gh_aiohttp
import asyncio
from dotenv import load_dotenv
from decouple import config


local_repo_directory = os.path.join(os.getcwd(), 'Clone_DBT_DEV')
destination = 'master'


def clone_repo():
    Repo.clone_from("https://github.com/Mauriciogc90Wize/airflow-dbt-demo.git", local_repo_directory,branch=destination)

def main():
    clone_repo()
    print("Hello")

if __name__ == "__main__":
    main()
