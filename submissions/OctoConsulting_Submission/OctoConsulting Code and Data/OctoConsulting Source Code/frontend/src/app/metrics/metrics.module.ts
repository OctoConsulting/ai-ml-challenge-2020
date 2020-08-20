import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MetricsRoutingModule } from './metrics-routing.module';
import { MetricsComponent } from './metrics.component';
import { MatCardModule } from '@angular/material';
import { APIService } from '../services/api.service';
import { MatTableModule } from '@angular/material/table';


@NgModule({
  declarations: [
    MetricsComponent,
  ],
  imports: [
    MetricsRoutingModule,
    MatTableModule,
    CommonModule,
    MatCardModule
  ],
  providers: [
    APIService
  ]
})
export class MetricsModule { }
