from pathlib import Path
from typing import Optional

import typer
from Database.database import StorageService
from Enums.enums import UserType
from Modals.UserModal import Driver, Rider

from bookMyTaxi import ERRORS, __app_name__, __version__, config
from bookMyTaxi.src.Database import database

store = StorageService

app = typer.Typer()

@app.command()
def RegisterNewDriver():
    typer.secho("Starting Registering process for the driver...")
    
    username=input("Enter driver name")
    # TODO: set this up in DB
    id=input("Enter id")
    email=input("Enter email address")
    password=input("Enter password")
    phone=input("Enter phone number")
    newDriver = Driver(username,id,password,phone,email)
    # wantsToRegisterVehicle = input("Would you like to register a vehicle")
    
    # TODO: improve this error handelling
    try:
        store.saveDriver(newDriver)
        
        # if(wantsToRegisterVehicle):
        #     typer.secho("Enter your vehicle ID for existing registered vehicle or first register your vehicle details to register ....")
        #     vehicleId = input("Enter vehicle ID")
        #     # TODO: search the vehicle id in db, if exist?add this to driver : prompt and exit
        #     try:
        #        
        #         pass
            
        #     except:
        #         typer.secho("Register driver failed while adding vehicle please try again ... aborting...")
        # else:
        typer.secho("Successfully registered new driver without vehicle")    
    except:
        typer.secho("registering new driver failed with some error ")


@app.command()
def RegisterNewRider():
    typer.secho("Starting Registering process for the Rider...")
    
    username=input("Enter rider name")
    # TODO: set this up in DB
    id=input("Enter id")
    email=input("Enter email address")
    password=input("Enter password")
    phone=input("Enter phone number")
    newRider = Rider(username,id,password,phone,email)
    
    # TODO: improve this error handelling
    try:
        store.saveDriver(newRider)
        typer.secho("Successfully registered new Rider")
    except:
        typer.secho("registering new driver failed with some error ")
    

@app.command()
def init(
    db_path: str = typer.Option(
        str(database.DEFAULT_DB_FILE_PATH),
        "--db-path",
        "-db",
        prompt="database location?",
    ),
) -> None:
    """Initialize the database."""
    app_init_error = config.init_app(db_path)
    if app_init_error:
        typer.secho(
            f'Creating config file failed with "{ERRORS[app_init_error]}"',
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)
    db_init_error = database.init_database(Path(db_path))
    if db_init_error:
        typer.secho(
            f'Creating database failed with "{ERRORS[db_init_error]}"',
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)
    else:
        typer.secho(f"The database is {db_path}", fg=typer.colors.GREEN)


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()

@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True,
    )
) -> None:
    return

