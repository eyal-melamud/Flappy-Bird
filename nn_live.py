# cd C:\PY\FB

import pygame as pg
from screen import Window
from bird import Bird
from pipe import Pipe
import sys
import neat
import itertools as itr

fps = 40
birds = []
ge = []
nets = []


def fitness_score(win: Window):
    return win.get_point() * 3 - 7


def remove_bird(i: int):
    birds.pop(i)
    ge.pop(i)
    nets.pop(i)


def eval_genomes(genomes, config):
    global birds, ge, nets, fps
    pg.init()
    win = Window(fps)
    clock = pg.time.Clock()
    diff = 75  # controls the intensity of the pipes
    count = diff
    con = True
    gap = Pipe().get_gap()
    max_score = 0
    fp = 0

    pipes = []
    birds = []
    ge = []
    nets = []

    for genome_id, genome in genomes:
        birds.append(Bird())
        ge.append(genome)
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        nets.append(net)
        genome.fitness = 0

    while con:
        con = len(birds) > 0

        # creates the pipes at a cetin rate.
        if count <= 0:
            pipes.append(Pipe())
            count = diff
        else:
            count -= 1

        # check if the player wants to quit.

        for event in pg.event.get():
            if event.type == pg.QUIT:
                print('gen - {0}.\nbest score - {1}'.format(pop.generation + 1, max_score))
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                fp = fps
                fps = win.hendel_buttons(event.pos[0], event.pos[1], fps)

        # checks if the first pipe is out of bounds
        if len(pipes) > 0 and pipes[0].get_x() <= -120:
            pipes = pipes[1:]

        # checks if the birds get stuck in pipes
        if fps == 0:
            for i, bird in enumerate(birds):
                ge[i].fitness += fitness_score(win)
            birds = []
            fps = fp

        elif len(pipes) > 0:
            for pi in pipes:

                for i, bird in enumerate(birds):
                    if bird.hit_detection(pi.get_pos(), pi.get_gap()) or bird.get_y() in [0, 645]:
                        ge[i].fitness += fitness_score(win)
                        remove_bird(i)
        else:
            for i, bird in enumerate(birds):
                if bird.get_y() in [0, 645]:
                    ge[i].fitness -= 10
                    remove_bird(i)
        max_score = win.get_point()

        for i, bird in enumerate(birds):
            if len(pipes) == 0:
                p_x = 450
                p_y = 400
            else:
                j = 0
                while pipes[j].get_x() < -62:
                    j += 1

                p_x, p_y = pipes[j].get_pos()
            output = nets[i].activate((bird.get_y(), bird.get_moment(), p_x, p_y, gap))
            if output[0] > 0.5:
                bird.jump()

        # prints the game

        win.print_screen(pipes, birds, pop.generation + 1)

        clock.tick(fps)
    print('gen - {0}.\nbest score - {1}'.format(pop.generation + 1, max_score))
    pg.quit()


def run(config_path):
    global pop
    # config_n = neat.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, config_path)
    # config_n =  neat.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, config_path)
    # config_n = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, config_path)
    config_n = neat.Config( neat.DefaultGenome, 
                            neat.DefaultReproduction, 
                            neat.DefaultSpeciesSet, 
                            neat.DefaultStagnation, 
                            config_path)
    pop = neat.Population(config_n)

    # Add a stdout reporter to show progress in the terminal.
    pop.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    pop.add_reporter(stats)
    pop.add_reporter(neat.Checkpointer(5))

    # run the game n times
    winner = pop.run(eval_genomes, 40)

    # Display the winning genome.
    print('\nBest genome:\n{!s}'.format(winner))

    # Show output of the most fit genome against training data.
    print('\nOutput:')
    pop.run(eval_genomes, 10)


def main():
    run('config.txt')


if __name__ == '__main__':
    main()
