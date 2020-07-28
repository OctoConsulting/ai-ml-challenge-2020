import { Component, OnInit, ViewEncapsulation, ViewChild } from '@angular/core';
import { MatStepper } from '@angular/material';

@Component({
  selector: 'app-stepper',
  templateUrl: './stepper.component.html',
  styleUrls: ['./stepper.component.scss'],
  encapsulation: ViewEncapsulation.None
})
export class StepperComponent implements OnInit {
  @ViewChild('stepper') stepper: MatStepper;
  public loadsUpload = true;
  public loadsNext = false;
  public showDone = false;
  public resId = null;
  public file = null;
  public result = null;

  constructor() { }

  ngOnInit() {
    // this.stepper.selectedIndex = 2;
    // this.file = true;
  }

  public onSelectionChange(event: any) {
    if (event.selectedIndex === 0) {
      this.loadsUpload = true;
      this.loadsNext = false;
      this.showDone = false;
    }
  }

  public onResIdSet(event: any) {
    this.resId = event;
  }

  public onUploadDone(event: any) {
    this.file = event;
    setTimeout( () => {
      this.loadsNext = true;
      this.loadsUpload = false;
      this.stepper.selectedIndex = 1;
    }, 1000);
  }

  public onAnalysisDone(event: any) {
    this.result = event;
    setTimeout( () => {
      this.stepper.selectedIndex = 2;
    }, 1000);
  }
}
