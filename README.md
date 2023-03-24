<a name="readme-top"></a>


<!-- PROJECT LOGO -->
<br />
<div align="center">
<!-- Logo goes here? -->

<h3 align="center">JH02</h3>

  <p align="center">
    An application to extract an area of Open Street Maps and style select, relevant features before serving out the result. Containerised through the use of Docker.
    <br />
    <a href="https://stgit.dcs.gla.ac.uk/team-project-h/2022/jh02/jh02-main"><strong>Explore the docs »</strong></a>
    <br />
    <br />
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li>
      <a href="#usage">Usage</a>
    </li>
    <li>
      <a href="#future-work">Future Work</a>
      <ul>
        <li><a href="#danger-zone">Danger Zone</a></li>
      </ul>
    </li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
The purpose of this project is to provide an end-to-end solution, enabling a user to extract a portion of Open Street Maps which can then be styled to their preference with Maputnik, before being served out as a Raster or Vector tile. <br/>
The initial extraction process fetches the selected area of the map and converts it from .pbf to .mbtiles using TileMaker. After styling it is served by TileServer. The application is run within a Docker container.

#### Built With

* Docker
* Flask
* Maputnik
* TileMaker
* TileServer
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started


#### Prerequisites

* Docker <br/>
  Download Docker Desktop from the following page: <br/>
  https://www.docker.com/products/docker-desktop/ <br/>
  Install using the terminal command
  ```
  "Docker Desktop Installer.exe" install
  ```
#### Installation

To install, clone the repository through the terminal by entering the following command:
``` 
git clone https://stgit.dcs.gla.ac.uk/team-project-h/2022/jh02/jh02-main.git
```
Make sure that Docker Desktop is open and running on the local machine. In the terminal, cd into the jh02-main/ directory, then run the commands:
```
docker compose build 
docker compose up
```
Now go to http://localhost:5001/ or http://127.0.0.1:5001 in a browser to see the application running.

If you encounter an 'Internal server error' when trying to style your selected map the first time you run the application, please try the following commands:
```
docker compose down
docker compose up
```
This error generally occurs due to TileServer exiting unexpectedly. After restarting the containers, the application should work as desired.

<!-- USAGE EXAMPLES -->
## Usage
#### Extracting Data:
From the homepage, navigate to the 'Data' page using the navbar. From the dropdown select the desired country .pbf file from GeoFabrik, press 'mbtiles' to download and convert the file to the correct format.
Once these are completed you will be automatically directed to the style page.
<br/><br/>
Note: Be aware that downloading large countries may take quite some time.

#### Styling the Map:
Again, navigate to the 'Style' page from the navbar, if not already there. Click 'Add Layer' within the Maputnik embed, and select 'map' as the data source. Choose the desired features and style them as preferred using the Maputnik UI. Multiple layers can be added as necessary. Follow the link [here](https://github.com/maputnik/editor/wiki) for the Maputnik documentation, if required.

#### Serving the Map:
When styling is complete, select the 'Serve' page in the navbar. The options will then be there to view the styled map as a vector or raster. Though TileServer will not automatically centre the map on the area selected, so it will have to be located manually.

 

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- FUTURE WORK -->
## Future Work

This project is intended as a prototype and there are several parts of it which can be expanded or improved upon. These are listed below.

<details>
  <summary>Ideas for future work on this project.</summary>
  <ol>
    <li>
      Add the option for a user to upload their own .osm.pbf file.
    </li>
    <li>
      Add the option to limit the bounding box for a selected country's map to style and view only particular parts.
    </li>
    <li>
      Get TileServer to automatically centre on/bound the styled area so that the user does not have to zoom into it manually.
    </li>
    <li>
      Add support for map area and feature extraction using Overpass Turbo.
    </li>
    <li>
      Create a viable default map.mbtiles option to circumvent the current requirement of running Docker twice on initial startup.
    </li>
    <li>
      Add a progress bar for downloading maps.
    </li>
  </ol>
</details>

#### Danger Zone

This section comprises the list of known issues and the list of things to be careful of when making changes to the project.

<details>
  <summary>Known issues.</summary>
  <ol>
    <li>
      On startup, TileServer throws an ERROR but does not exit.
    </li>
    <li>
      Occasionally Docker Daemon will refuse to build for no apparent reason.
    </li>
    <li>
      When trying to download the map of a very large country, GeoFabrik's servers may time out. If this happens the resulting process file in the data volume must be deleted before TileServer works again.
    </li>
  </ol>
</details>



<details>
  <summary>Be careful of these when making changes.</summary>
  <ol>
    <li>
      If any changes are made to the run.sh file which moves folders into the correct volumes on startup, these must be made with the end of line sequence set to 'LF'. If the end of line sequence is set to 'CRLF', the build will fail.
    </li>
  </ol>
</details>


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [MapTiler](https://github.com/maptiler/tileserver-gl)
* [Systemed](https://github.com/systemed/tilemaker)
* [Maputnik](https://github.com/maputnik/editor)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
<!-- example -->
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
