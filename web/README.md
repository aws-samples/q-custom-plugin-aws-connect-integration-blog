# BankingWebsite

This project was generated with [Angular CLI](https://github.com/angular/angular-cli) version 15.2.6.

## Web Application Overview

The /web folder contains an Angular-based web application for a banking website. This single-page application provides various banking features and functionalities, including:

- Account management
- Transaction history
- Loan services
- Investment options
- Chat support

The application is built using Angular 15 and follows a component-based architecture for modular and maintainable code.

## Development server

Run `ng serve` for a dev server. Navigate to `http://localhost:4200/`. The application will automatically reload if you change any of the source files.

To run the application in production mode, use `ng serve --configuration=production`. This will apply production-specific optimizations and settings as defined in the angular.json file.

## Code scaffolding

Run `ng generate component component-name` to generate a new component. You can also use `ng generate directive|pipe|service|class|guard|interface|enum|module`.

## Build

Run `ng build` to build the project. The build artifacts will be stored in the `dist/` directory.

## Running unit tests

Run `ng test` to execute the unit tests via [Karma](https://karma-runner.github.io).

## Running end-to-end tests

Run `ng e2e` to execute the end-to-end tests via a platform of your choice. To use this command, you need to first add a package that implements end-to-end testing capabilities.

## Project Structure

The web application follows a standard Angular project structure:

- `src/app`: Contains the main application code
  - `accounts`: Component for managing user accounts
  - `chat`: Component for chat support
  - `footer`: Footer component
  - `header`: Header component
  - `home`: Home page component
  - `investments`: Component for investment options
  - `loans`: Component for loan services
  - `transactions`: Component for transaction history
- `src/assets`: Static assets and environment-specific configuration
- `src/environments`: Environment-specific configuration files
- `angular.json`: Angular CLI configuration file
- `Dockerfile`: Docker configuration for containerizing the application
- `tsconfig.json`: TypeScript configuration file

The application uses Angular Material for UI components and follows the pink-bluegrey theme.

## Further help

To get more help on the Angular CLI use `ng help` or go check out the [Angular CLI Overview and Command Reference](https://angular.io/cli) page.