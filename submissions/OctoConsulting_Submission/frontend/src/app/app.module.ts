import { NgModule } from '@angular/core';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { BrowserModule } from '@angular/platform-browser';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { NavbarComponent } from './navbar/navbar.component';
import {
  HttpClientModule
} from '@angular/common/http';




import {
  MatButtonModule,
  MatProgressBarModule,
  MatToolbarModule,
  MatIconModule,
  MatTabsModule,
  MatProgressSpinnerModule,
  MatSelectModule
} from '@angular/material';
import { EncryptionService } from './services/end-dec.service';
import { FooterComponent } from './footer/footer.component';


@NgModule({
  declarations: [
    AppComponent,
    NavbarComponent,
    FooterComponent
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    AppRoutingModule,
    HttpClientModule,
    MatButtonModule,
    MatProgressBarModule,
    MatToolbarModule,
    MatIconModule,
    MatTabsModule,
    MatProgressSpinnerModule,
    MatSelectModule
  ],
  providers: [EncryptionService],
  bootstrap: [AppComponent]
})
export class AppModule { }
