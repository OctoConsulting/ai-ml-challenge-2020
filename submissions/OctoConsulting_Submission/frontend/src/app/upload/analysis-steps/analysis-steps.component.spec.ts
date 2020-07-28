import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { AnalysisStepsComponent } from './analysis-steps.component';

describe('AnalysisStepsComponent', () => {
  let component: AnalysisStepsComponent;
  let fixture: ComponentFixture<AnalysisStepsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ AnalysisStepsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(AnalysisStepsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
