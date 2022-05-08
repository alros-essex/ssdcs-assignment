import {Component, OnInit} from '@angular/core';
import {RestClientService} from '../rest-client.service';
import {Experiments} from './experiments';
import {Measure} from '../measure';

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

  constructor(private rest: RestClientService) {
  }

  // declaring a variable and get the rest service to assign measures to the variable
  // subscribe to show an error
  getexperiments(): void {
    this.rest.get_experiments().subscribe(e => this.experiments = e);
  }

  // get_measure_for_experiment(experimentId: string): Measure {
  //   let measure;
  //   this.rest.get_measure_for_experiment(experimentId)
  //     .subscribe(m => measure = m);
  //
  //   return measure;
  // }

  save_experiment(): void {
    console.log(`Saving new experiment ${this.newExperiment.name}`);
    this.rest.save_experiment(this.newExperiment.name);
  }

  ngOnInit(): void {
  }

}


