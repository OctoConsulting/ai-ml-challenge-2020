import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { UploadComponent } from './upload.component';
import {
  MatCardModule,
  MatFormFieldModule,
  MatSelectModule,
  MatInputModule,
  MatButtonModule,
  MatProgressBarModule,
  MatToolbarModule,
  MatSidenavModule,
  MatIconModule,
  MatListModule,
  MatPaginatorModule,
  MatTableModule,
  MatProgressSpinnerModule,
  MatStepperModule
} from '@angular/material';

import {
  ReactiveFormsModule,
  FormsModule
} from '@angular/forms';

import {
  HttpClientModule
} from '@angular/common/http';
import { MatFileUploadModule } from 'angular-material-fileupload';
import { UploadRoutingModule } from './upload-routing.module';
import { StepperComponent } from './stepper/stepper.component';
import { UploadFormComponent } from './upload-form/upload-form.component';
import { AnalysisStepsComponent } from './analysis-steps/analysis-steps.component';
import { ResultsComponent } from './results/results.component';
import { PdfViewerModule } from 'ng2-pdf-viewer';
import { APIService } from '../services/api.service';





@NgModule({
  declarations: [
    UploadComponent,
    StepperComponent,
    UploadFormComponent,
    AnalysisStepsComponent,
    ResultsComponent
  ],
  imports: [
    UploadRoutingModule,
    CommonModule,
    FormsModule,
    ReactiveFormsModule,
    MatToolbarModule,
    MatSidenavModule,
    MatIconModule,
    MatPaginatorModule,
    MatProgressBarModule,
    MatProgressSpinnerModule,
    MatFormFieldModule,
    MatSelectModule,
    MatInputModule,
    MatButtonModule,
    MatTableModule,
    HttpClientModule,
    MatListModule,
    MatFileUploadModule,
    MatCardModule,
    MatStepperModule,
    PdfViewerModule
  ],
  providers: [
    APIService
  ]
})
export class UploadModule { }
