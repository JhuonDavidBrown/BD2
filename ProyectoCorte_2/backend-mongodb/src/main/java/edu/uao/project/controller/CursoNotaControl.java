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

import edu.uao.project.model.CursoNota;
import edu.uao.project.service.CursoNotaServiceIMPL;
import lombok.RequiredArgsConstructor;

@RestController
@RequestMapping("/api/v4")
@RequiredArgsConstructor
public class CursoNotaControl {
	
	private final CursoNotaServiceIMPL cursoNotaService;
	
	@PostMapping("/CoursesRating")
	public void save(@RequestBody CursoNota cursoNota) {
		cursoNotaService.save(cursoNota);
	}
	
	@GetMapping("/CoursesRating")
	public List<CursoNota> findAll(){
		return cursoNotaService.findAll();
	}
	
	@GetMapping("/CoursesRating/{id}")
	public CursoNota findById(@PathVariable String id) {
		return cursoNotaService.findById(id).get();
	}
	@DeleteMapping("/CoursesRating/{id}")
	public void deleteById(@PathVariable String id) {
		cursoNotaService.deleteById(id);
	}
	@PutMapping("/CoursesRating")
	public void update(@RequestBody CursoNota cursoNota) {
		cursoNotaService.save(cursoNota);
		
	}
}
