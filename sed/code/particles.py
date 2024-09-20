import pygame
from support import import_folder
from random import choice


class AnimationPlayer:
    def __init__(self):
        self.frames = {
            # magic
            'bubble': import_folder('../graphics/particles/bubble/frames'),
            'aura': import_folder('../graphics/particles/aura'),
            'heal': import_folder('../graphics/particles/heal/frames'),

            # attacks
            'claw': import_folder('../graphics/particles/claw'),
            'slash': import_folder('../graphics/particles/slash'),
            'sparkle': import_folder('../graphics/particles/sparkle'),
            'cyclops_attack': import_folder('../graphics/particles/cyclops_attack'),
            'thunder': import_folder('../graphics/particles/thunder'),

            # monster deaths
            'octopus': import_folder('../graphics/particles/smoke_orange'),
            'patrick_starts': import_folder('../graphics/particles/raccoon'),
            'spirit': import_folder('../graphics/particles/nova'),
            'cyclops': import_folder('../graphics/particles/bird'),

            # leafs
            'seaweeds': (
                import_folder('../graphics/particles/bubble/frames'),
                import_folder('../graphics/particles/leaf2'),
            )
        }

    def create_grass_particles(self, pos, groups):
        animation_frames = choice(self.frames['seaweeds'])
        ParticleEffect(pos, animation_frames, groups)

    def create_particles(self, animation_type, pos, groups):
        animation_frames = self.frames[animation_type]
        ParticleEffect(pos, animation_frames, groups)


class ParticleEffect(pygame.sprite.Sprite):
    def __init__(self, pos, animation_frames, groups):
        super().__init__(groups)
        self.sprite_type = 'magic'
        self.frame_index = 0
        self.animation_speed = 0.15
        self.frames = animation_frames
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(center=pos)

    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.frames):
            self.kill()
        else:
            self.image = self.frames[int(self.frame_index)]

    def update(self):
        self.animate()
