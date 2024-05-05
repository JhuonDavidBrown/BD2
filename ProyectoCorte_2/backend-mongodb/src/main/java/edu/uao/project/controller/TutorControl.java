package edu.uao.project.controller;

import java.util.List;

import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import edu.uao.project.model.Tutor;
import edu.uao.project.service.TutorServiceIMPL;
import lombok.RequiredArgsConstructor;

@RestController
@RequestMapping("/api/v3")
@RequiredArgsConstructor
public class TutorControl {
	
	private final TutorServiceIMPL tutorService;
	
	@PostMapping("/Tutors")
	public void save(@RequestBody Tutor tutor) {
		tutorService.save(tutor);
	}
	@GetMapping("/Tutors")
	public List<Tutor> findAll(){
		return tutorService.findAll();
	}
	@GetMapping("/Tutors/{id}")
	public Tutor findById(@PathVariable String id) {
		return tutorService.findById(id).get();
	}
	@DeleteMapping("/Tutors/{id}")
	public void deleteById(@PathVariable String id) {
		tutorService.deleteById(id);
	}
	@PutMapping("/Tutors")
	public void update(@RequestBody Tutor tutor) {
		tutorService.save(tutor);	
	}
}