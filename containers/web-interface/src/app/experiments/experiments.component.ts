import {Component, OnInit} from '@angular/core';
import {RestClientService} from '../rest-client.service';
import {Experiments} from './experiments';
import {AuthUtilsService} from '../auth-utils.service';

@Component({
  selector: 'app-experiments',
  templateUrl: './experiments.component.html',
  styleUrls: ['./experiments.component.css']
})
export class ExperimentsComponent implements OnInit {

  experiments: Experiments[] = [];
  newExperiment: Experiments = {
    experiment_id: '',
    name: ''
  };

  constructor(private rest: RestClientService, private authService: AuthUtilsService) {
  }

  // declaring a variable and get the rest service to assign measures to the variable
  // subscribe to show an error
  getexperiments(): void {
    this.rest.get_experiments().subscribe(e => {
      this.experiments = e.sort((a, b) => a.experiment_id > b.experiment_id ? 1 : -1);
    });
  }

  save_experiment(): void {
    console.log(`Saving new experiment ${this.newExperiment.name}`);
    this.rest.save_experiment(this.newExperiment.name);
  }

  ngOnInit(): void {
    this.getexperiments();
  }

  isUserAdmin(): boolean {
    return this.authService.isLoggedInUserAdmin();
  }

  isUserScientist(): boolean {
    return this.authService.isLoggedInUserScientist();
  }
}


