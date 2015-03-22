class StatsService
  def all_stats
    Player.all.map do |p|
      {
        nickname: p.nickname,
        win_percentage: Game.win_percentage_for_player(p),
        goals_scored: Game.goals_scored_for_player(p),
        goals_against: Game.goals_against_for_player(p)
      }
    end
  end
end
