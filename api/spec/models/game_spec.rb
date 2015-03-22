require "rails_helper"

RSpec.describe Game do
  it "returns false when there is no active game" do
    expect(Game.in_progress?).to eq false
  end

  it "returns true when a game is in progress" do
    Game.create(
      team_1_score: 0,
      team_2_score: 0,
      in_progress: true,
      team_1_defense_id: 123,
      team_1_offense_id: 123,
      team_2_offense_id: 987,
      team_2_defense_id: 987
    )

    expect(Game.in_progress?).to eq true
  end

  it "counts the goals a player has scored when on offense" do
    player_1 = Player.create(nickname: "Fuzzy Pants")
    player_2 = Player.create(nickname: "Golden Pants")

    Game.create(
      team_1_score: 5,
      team_2_score: 3,
      in_progress: false,
      team_1_defense_id: player_1.id,
      team_1_offense_id: player_1.id,
      team_2_offense_id: player_2.id,
      team_2_defense_id: player_2.id
    )

    expect(Game.goals_scored_for_player(player_1.id)).to eq 5
    expect(Game.goals_scored_for_player(player_2.id)).to eq 3
  end

  it "counts the goals against a player on defense" do
    player_1 = Player.create(nickname: "Fuzzy Pants")
    player_2 = Player.create(nickname: "Golden Pants")

    Game.create(
      team_1_score: 2,
      team_2_score: 5,
      in_progress: false,
      team_1_defense_id: player_1.id,
      team_1_offense_id: player_1.id,
      team_2_offense_id: player_2.id,
      team_2_defense_id: player_2.id
    )

    expect(Game.goals_against_for_player(player_1.id)).to eq 5
    expect(Game.goals_against_for_player(player_2.id)).to eq 2
  end

  it "calculates the win percentage for a player" do
    player_1 = Player.create(nickname: "Fuzzy Pants")
    player_2 = Player.create(nickname: "Golden Pants")

    Game.create(
      team_1_score: 5,
      team_2_score: 0,
      in_progress: false,
      team_1_defense_id: player_1.id,
      team_1_offense_id: player_1.id,
      team_2_offense_id: player_2.id,
      team_2_defense_id: player_2.id
    )

    Game.create(
      team_1_score: 0,
      team_2_score: 5,
      in_progress: false,
      team_1_defense_id: player_1.id,
      team_1_offense_id: player_1.id,
      team_2_offense_id: player_2.id,
      team_2_defense_id: player_2.id
    )

    expect(
      Game.win_percentage_for_player(player_id = player_1.id)
    ).to eq 50
  end

  it "does not divide by zero when no games have been played" do
    player_1 = Player.create(nickname: "Fuzzy Pants")

    expect(
      Game.win_percentage_for_player(player_id = player_1.id)
    ).to eq 0
  end
end
