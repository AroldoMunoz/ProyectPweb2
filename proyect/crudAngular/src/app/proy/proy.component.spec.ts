import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ProyComponent } from './proy.component';

describe('ProyComponent', () => {
  let component: ProyComponent;
  let fixture: ComponentFixture<ProyComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ProyComponent]
    });
    fixture = TestBed.createComponent(ProyComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
