import { Component, OnInit } from '@angular/core';
import { Tutorial } from '../../models/tutorial.model';
import { TutorialService } from '../../services/tutorial.service';

/**
 * @Component decorator provides metadata about the component, 
 * such as its selector, template URL, and styles.
 */
@Component({
  selector: 'app-tutorials-list',
  templateUrl: './tutorials-list.component.html',
  styleUrls: ['./tutorials-list.component.css'],
})
export class TutorialsListComponent implements OnInit {
  tutorials?: Tutorial[]; // Array to hold the list of tutorials
  currentTutorial: Tutorial = {}; // Object to hold the currently selected tutorial
  currentIndex = -1; // Index of the currently selected tutorial
  title = ''; // Title to search for tutorials

  /**
   * Constructor to inject the TutorialService dependency
   * @param tutorialService - Service to handle tutorial-related operations
   */
  constructor(private tutorialService: TutorialService) {}

  /**
   * Lifecycle hook that is called after data-bound properties of a directive are initialized.
   * Here, it is used to retrieve the list of tutorials when the component is initialized.
   */
  ngOnInit(): void {
    this.retrieveTutorials();
  }

  /**
   * Method to retrieve all tutorials from the service.
   * It subscribes to the observable returned by the service and assigns the data to the tutorials array.
   */
  retrieveTutorials(): void {
    this.tutorialService.getAll().subscribe({
      next: (data) => {
        this.tutorials = data;
        console.log(data);
      },
      error: (e) => console.error(e)
    });
  }

  /**
   * Method to refresh the list of tutorials.
   * It retrieves the tutorials again and resets the current tutorial and index.
   */
  refreshList(): void {
    this.retrieveTutorials();
    this.currentTutorial = {};
    this.currentIndex = -1;
  }

  /**
   * Method to set the currently active tutorial.
   * @param tutorial - The tutorial object to set as active
   * @param index - The index of the tutorial in the list
   */
  setActiveTutorial(tutorial: Tutorial, index: number): void {
    this.currentTutorial = tutorial;
    this.currentIndex = index;
  }

  /**
   * Method to remove all tutorials.
   * It calls the service to delete all tutorials and refreshes the list upon success.
   */
  removeAllTutorials(): void {
    this.tutorialService.deleteAll().subscribe({
      next: (res) => {
        console.log(res);
        this.refreshList();
      },
      error: (e) => console.error(e)
    });
  }

  /**
   * Method to search for tutorials by title.
   * It calls the service to find tutorials by title and assigns the data to the tutorials array.
   */
  searchTitle(): void {
    this.currentTutorial = {};
    this.currentIndex = -1;

    this.tutorialService.findByTitle(this.title).subscribe({
      next: (data) => {
        this.tutorials = data;
        console.log(data);
      },
      error: (e) => console.error(e)
    });
  }
}
