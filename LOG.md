# LOG.md

## Daily Scrum - 01/03/26

### Full Team (Product Owner, Scrum Master, T.L and Developers)

- What we did today:
  We met to plan the work distribution. We conducted a self-assessment of each team member's knowledge level to assign files according to their complexity.

- What we will do tomorrow:
  Start implementing the base logic in `inicio.py` to establish the main game variables and allow subsequent integration with other modules.

- Blockers:
  No blockers were presented.


---

## Daily Scrum - 02/03/26

### Deyanis and Laimen (inicio.py)

- What we did today:
  We defined the initial game variables. We implemented difficulty validation and resource assignment based on the chosen level. We also requested the user's name and difficulty via `input`.

- What we will do tomorrow:
  Integrate consumption and state logic within the main game loop.

- Blockers:
  No blockers were presented.


### Melissa (motor.py)

- What I did today:
  I created the `motor.py` file and started importing the `inicio.py` module to access its variables and begin structuring the main loop that orchestrates the game.

- What I will do tomorrow:
  Support other team members in structuring their modules to facilitate integration with the main engine.

- Blockers:
  Yes.

- Reason:
  The developed code is only in the local environment and could not be uploaded to GitHub, which hinders team integration.

### Saul (eventos.py)

- What I did today:
  No progress was made on the assigned module because we were waiting for the final definition of the main game flow in `inicio.py` and `motor.py`.

- What I will do tomorrow:
  Start structuring the daily events logic and define possible random scenarios.

- Blockers:
  Yes.
  Dependency on the base engine structure to ensure compatibility.


### Angela (consumo.py)

- What I did today:
  No technical progress was made. The functional requirements of the consumption module were reviewed to plan the implementation.

- What I will do tomorrow:
  Implement the logic for daily resource reduction based on the defined population.

- Blockers:
  No.


### Elianis (interfaz.py)

- What I did today:
  No progress was recorded because the visual design depends on the final output structure defined in the main engine.

- What I will do tomorrow:
  Design the base structure of visual tables and initial tests with console formatting.

- Blockers:
  Yes.
  Partial dependency on the main game flow.


### Gustavo (README.md)

- What I did today:
  A general review of the project was conducted to begin structuring the technical documentation, I supervised the pushes to the dev branch, to perform merges without generating conflicts.

- What I will do tomorrow:
  Write the initial README section with project description and objectives.

- Blockers:
  No.


---

## Daily Scrum - 03/03/26

### Deyanis and Laimen (inicio.py)

- What we did today:
  We refactored unnecessary variables, translated the code to English to maintain technical coherence, and sent the changes to the repository.

- What we will do tomorrow:
  Improve internal code documentation, remove redundant comments, and simplify logic where possible.

- Blockers:
  No blockers were presented.

### Saul (eventos.py)

- What I did today:
  The base structure of the events module was defined and possible event types were proposed (negative or no event).

- What I will do tomorrow:
  Implement the daily random generation function.

- Blockers:
  No.


### Angela (consumo.py)

- What I did today:
  The base logic for calculating daily resource consumption based on population was designed.

- What I will do tomorrow:
  Integrate initial tests of the calculation with simulated values.

- Blockers:
  No.


### Elianis (interfaz.py)

- What I did today:
  Initial console formatting tests and data presentation structure were performed, files could not be uploaded due to a git problem, changes remained on the local machine.

- What I will do tomorrow:
  Adjust the visual design to improve clarity in resource and status presentation.

- Blockers:
  Yes.
  Git problem that prevented uploading changes to the repository.


### Gustavo (README.md)

- What I did today:
  The README drafting began, including a general game description and project structure.

- What I will do tomorrow:
  Add installation and execution section.

- Blockers:
  No.

### Juan (estado.py)

- What I did today:
  I joined the development team and reviewed the current project structure to understand the architecture and responsibilities of each module.

- What I will do tomorrow:
  Start implementing the `estado.py` module, defining the main game validations.

- Blockers:
  No.

---

## Daily Scrum - 04/03/26

### Deyanis and Laimen (inicio.py)

- What we did today:
  The structure of the `inicio.py` module was improved, simplifying difficulty validation and adjusting function typing to facilitate integration with other game modules.

- What we will do tomorrow:
  Perform integration tests with the engine and validate correct resource initialization.

- Blockers:
  No blockers were presented.


### Juan (estado.py)

- What I did today:
  I implemented the `verify_state` function, establishing resource normalization for negative values and defining player defeat conditions.

- What I will do tomorrow:
  Integrate state validation within the main engine cycle and perform functionality tests.

- Blockers:
  No blockers were presented.


### Saul (eventos.py)

- What I did today:
  I implemented random event generation and the logic for applying effects based on the selected difficulty.

- What I will do tomorrow:
  Adjust the interaction between events and the state module to validate conditions after each event.

- Blockers:
  No blockers were presented.


### Angela (consumo.py)

- What I did today:
  I implemented the initial logic for calculating resource consumption based on the player's population.

- What I will do tomorrow:
  Integrate the module with the main engine and validate that consumption is applied correctly each day of the cycle.

- Blockers:
  Yes.
  It was not possible to push to the repository due to a Git authentication problem. Changes remain in the local environment.


### Elianis (interfaz.py)

- What I did today:
  I implemented the initial console printing structure using `colorama` to improve the game's visual appearance. Conditionals were added to change color based on available resources.

- What I will do tomorrow:
  Adjust the visual presentation to integrate with real data generated by the game engine.

- Blockers:
  Yes.
  Git authentication problem that prevented uploading changes to the repository.


### Melissa (motor.py)

- What I did today:
  I advanced in the main game cycle structure, defining the day loop and preparing integration with events, consumption, and state modules.

- What I will do tomorrow:
  Complete module integration and validate the complete game flow.

- Blockers:
  No blockers were presented.


### Gustavo (Scrum Master / README)

- What I did today:
  I performed a technical review of the developed modules to ensure coherence in structure, typing, and general project flow. I supervised the commit status and supported in resolving Git-related problems.

- What I will do tomorrow:
  Coordinate the integration of pending modules and continue with project documentation.

- Blockers:
  No.


### Gustavo (Scrum Master / README)

- What I did today:
  I reviewed the repository branch structure and consolidated development in the `dev` branch, eliminating the already integrated `feature/*` branches to simplify the workflow. Main modules were synchronized and remote repository updates were verified.

- What I will do tomorrow:
  Coordinate the final integration between modules and continue with the project's technical documentation.

- Blockers:
  No.
 
---

## Daily Scrum - 05/03/26


### Full Team (Product Owner, Scrum Master, T.L and Developers)

- What we did today:
  We met to define a new workflow in the repository. 
  Since the `feature/*` branches were eliminated, it was agreed that from now on all developers will work directly on the `dev` branch, modifying only the file corresponding to their assigned module.

- What we will do tomorrow:
  Present to the client an **MVP (Minimum Viable Product)** of the game with the main modules integrated.

- Blockers:
  No blockers were presented.


### Saul (eventos.py)

- What I did today:
  I documented the `eventos.py` module code, adding English comments to improve understanding of the implemented logic.

- What I will do tomorrow:
  Implement the use of the `max()` function to avoid negative resource values when events occur. Also, evaluate the use of `colorama` to improve event visualization in the console.

- Blockers:
  No.


### Angela (consumo.py)

- What I did today:
  I implemented the `consume` and `market_logic` functions to handle daily resource consumption logic and market actions based on wheat price.

- What I will do tomorrow:
  Review possible improvements in consumption logic and validate correct integration with the game engine.

- Blockers:
  No.


### Elianis (interfaz.py)

- What I did today:
  I continued working on the game's console visual presentation, using `colorama` to differentiate resources by colors and improve the clarity of information shown to the player.

- What I will do tomorrow:
  Adjust the interface to integrate with data generated by the game engine and other modules.

- Blockers:
  No.


### Melissa (motor.py)

- What I did today:
  I continued integrating the different game modules within the main engine loop, verifying that execution follows the correct order between events, consumption, and state verification.

- What I will do tomorrow:
  Perform complete game execution tests to validate the day cycle flow.

- Blockers:
  No.


### Juan (estado.py)

- What I did today:
  I reviewed the player state validation logic and adjusted defeat conditions to ensure coherence with changes made in other modules.

- What I will do tomorrow:
  Perform additional tests to ensure victory or defeat conditions are evaluated correctly.

- Blockers:
  No.


### Gustavo (Scrum Master / README)

- What I did today:
  I performed a general code review of the project to ensure coherence between modules. 
  Refactorings were applied in `inicio.py`, `estado.py`, `eventos.py`, and `consumo.py`, replacing the use of lists with dictionaries to improve readability and code maintenance. 
  **Docstrings** were also added to functions to standardize internal project documentation.
  The repository was synchronized with the project's dev branch and merge conflicts in `consumo.py` were resolved.

- What I will do tomorrow:
  Coordinate the **MVP** presentation to the client and continue improving project documentation.

- Blockers:
  No.

## Daily Scrum - 06/03/26

### Full Team (Product Owner, Scrum Master, T.L and Developers)

- What we did today:
  We presented the **MVP of the game** to the client, demonstrating the integration of the main modules and the basic gameplay loop. 
  The client provided positive feedback and suggested improvements related to gameplay balance and interface clarity.

- What we will do tomorrow:
  Continue improving the consumption system and implement daily modifiers depending on the day of the week.

- Blockers:
  No technical blockers were reported.


### Gustavo (Scrum Master / README)

- What I did today:
  I coordinated the MVP presentation and helped organize the remaining improvements that the team needed to implement after the client's feedback.

- What I will do tomorrow:
  Continue improving the project documentation and start preparing a `tests.py` file to validate the main game functions.

- Blockers:
  I experienced a minor emotional blocker because our team was not called to present directly like other teams, but I refocused on coordinating improvements for the project.

## Daily Scrum - 07/03/26

### Full Team (Product Owner, Scrum Master, T.L and Developers)

- What we did today:
  The team continued improving the internal logic of the game after the MVP presentation. 
  Several refactors were applied to improve code structure, fix return types in the game engine, and implement the daily consumption modifier based on the day of the week.

- What we will do tomorrow:
  Continue testing the game loop and ensure all modules interact correctly before the next iteration.

- Blockers:
  No blockers were reported.

### Angela (consumo.py)

- What I did today:
  I implemented the **daily resource consumption modifier** depending on the day of the week and removed the rationing system to simplify the gameplay logic. 
  I also adjusted the `consume()` function to integrate the new modifier and updated the market logic accordingly.

- What I will do tomorrow:
  Continue testing the consumption system to ensure the modifiers work correctly and maintain game balance.

- Blockers:
  No.

### Saul (eventos.py)

- What I did today:
  I implemented color visualization for resource loss during events using `colorama` to improve the console feedback shown to the player.

- What I will do tomorrow:
  Continue reviewing the event system and ensure events correctly affect the resource values.

- Blockers:
  No.

### Melissa (motor.py)

- What I did today:
  I corrected the `init_engine()` function return type and refactored the main game loop by removing an unnecessary `break` statement in the `day_cycle` logic.

- What I will do tomorrow:
  Continue validating the game engine integration with the rest of the modules.

- Blockers:
  No.

### Elianis (interfaz.py)

- What I did today:
  I continued improving the console interface and adjusted the resource display formatting to make the game information clearer for the player.

- What I will do tomorrow:
  Integrate additional interface improvements and verify compatibility with the game engine output.

- Blockers:
  No.

### Gustavo (Scrum Master / README)

- What I did today:
  I reviewed the repository commits and ensured that the refactors and fixes made by the team were properly integrated into the `dev` branch.

- What I will do tomorrow:
  Continue monitoring the project progress and help maintain documentation consistency across modules.

- Blockers:
  No.