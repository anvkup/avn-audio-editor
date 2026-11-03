from avn_auto_editor.core.models import ProductionProject
from avn_auto_editor.core.pipeline import ProcessingPipeline


def test_pipeline_summary_and_queue():
    project = ProductionProject(name="Test Project", root="/tmp/test-project")
    pipeline = ProcessingPipeline(project)

    summary = pipeline.summary()
    assert "completion" in summary
    assert "average_confidence" in summary
    assert len(pipeline.queue_items()) >= 1

    pipeline.advance("REAPER export", True, "Project exported", 0.93)
    assert pipeline.stages[-1].complete is True
