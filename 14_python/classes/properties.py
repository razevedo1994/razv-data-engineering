from dataclasses import dataclass, field


@dataclass
class VideoClip:
    minutes: int
    seconds: int
    title: str

    @property
    def duration(self) -> int:
        return self.minutes * 60 + self.seconds
    
    @duration.setter
    def duration(self, seconds: int) -> None:
        self.minutes, self.seconds = divmod(seconds, 60)


@dataclass
class VideoProject:
    clips: list[VideoClip] = field(default_factory=list)
    title: str = "Untitled"

    @property
    def total_length(self) -> int:
        return sum([clip.minutes * 60 + clip.seconds for clip in self.clips])
    

def main() -> None:
    clip1 = VideoClip(minutes=1, seconds=30, title="Clip 1")
    clip2 = VideoClip(minutes=2, seconds=30, title="Clip 2")
    project = VideoProject(clips=[clip1, clip2], title="My Project")
    print(project.total_length)
    clip1.duration = 120
    print(project.total_length)


if __name__ == "__main__":
    main()